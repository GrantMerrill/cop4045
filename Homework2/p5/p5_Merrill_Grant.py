import datetime
import os
import sys
import tempfile
import unittest


def read_observations(filename):
	observations = {}
	errors = []
	seen = set()

	with open(filename, "r") as file:
		for line_number, line in enumerate(file, start=1):
			fields = [field.strip() for field in line.strip().split(",")]

			if len(fields) != 3 or not fields[0] or not fields[1] or not fields[2]:
				errors.append((line_number, "malformed line"))
				continue

			station, date_text, temperature_text = fields

			try:
				date = datetime.datetime.strptime(date_text, "%I:%M:%S %p %m/%d/%Y")
			except ValueError:
				errors.append((line_number, "invalid date"))
				continue

			try:
				temperature = float(temperature_text)
			except ValueError:
				errors.append((line_number, "invalid temperature"))
				continue

			if not -100.0 <= temperature <= 150.0:
				errors.append((line_number, "temperature out of range"))
				continue

			key = (station, date)
			if key in seen:
				errors.append((line_number, "duplicate station/date combination"))
				continue

			seen.add(key)
			observations.setdefault(station, []).append((date, temperature))

	for station_observations in observations.values():
		station_observations.sort(key=lambda observation: observation[0])

	return observations, errors


def station_statistics(observations):
	statistics = {}

	for station, station_observations in observations.items():
		temperatures = [temperature for _, temperature in station_observations]
		statistics[station] = {
			"min": min(temperatures),
			"max": max(temperatures),
			"mean": sum(temperatures) / len(temperatures),
		}

	return statistics


def station_outliers(observations):
	statistics = station_statistics(observations)
	outliers = {
		station: (date, temperature, statistics[station]["mean"])
		for station, station_observations in observations.items()
		for date, temperature in [station_observations[-1]]
		if temperature > statistics[station]["mean"]
	}

	return outliers


def write_statistics(filename, statistics):
	with open(filename, "w") as file:
		for station in sorted(statistics):
			station_statistics = statistics[station]
			file.write(
				f"{station},{station_statistics['min']:.1f},"
				f"{station_statistics['max']:.1f},{station_statistics['mean']:.1f}\n"
			)


def main():
	if len(sys.argv) != 3:
		print("Usage: python p5_Merrill_Grant.py observations.txt statistics.txt")
		return

	observations_filename = sys.argv[1]
	statistics_filename = sys.argv[2]

	try:
		observations, errors = read_observations(observations_filename)
		statistics = station_statistics(observations)
		outliers = station_outliers(observations)

		print(statistics)
		print(outliers)
		if errors:
			print(errors)

		write_statistics(statistics_filename, statistics)
	except OSError as error:
		print(f"File access error: {error}")


class TestWeatherObservations(unittest.TestCase):
	def create_observation_file(self, contents):
		file = tempfile.NamedTemporaryFile(mode="w", delete=False)
		file.write(contents)
		file.close()
		self.addCleanup(os.unlink, file.name)
		return file.name

	def test_several_stations(self):
		filename = self.create_observation_file(
			"North, 09:00:00 AM 04/20/2026, 65\n"
			"South, 10:00:00 AM 04/20/2026, 70\n"
		)

		observations, errors = read_observations(filename)

		self.assertEqual(errors, [])
		self.assertEqual(observations["North"][0][1], 65.0)
		self.assertEqual(observations["South"][0][1], 70.0)

	def test_negative_temperatures(self):
		filename = self.create_observation_file(
			"North, 09:00:00 AM 04/20/2026, -12.5\n"
		)

		observations, errors = read_observations(filename)

		self.assertEqual(errors, [])
		self.assertEqual(observations["North"][0][1], -12.5)

	def test_duplicate_observations(self):
		filename = self.create_observation_file(
			"North, 09:00:00 AM 04/20/2026, 65\n"
			"North, 09:00:00 AM 04/20/2026, 66\n"
		)

		observations, errors = read_observations(filename)

		self.assertEqual(len(observations["North"]), 1)
		self.assertEqual(errors, [(2, "duplicate station/date combination")])

	def test_invalid_temperature_ranges_and_boundaries(self):
		filename = self.create_observation_file(
			"Low, 09:00:00 AM 04/20/2026, -100.0\n"
			"High, 09:00:00 AM 04/20/2026, 150.0\n"
			"TooLow, 09:00:00 AM 04/20/2026, -100.1\n"
			"TooHigh, 09:00:00 AM 04/20/2026, 150.1\n"
		)

		observations, errors = read_observations(filename)

		self.assertEqual(observations["Low"][0][1], -100.0)
		self.assertEqual(observations["High"][0][1], 150.0)
		self.assertNotIn("TooLow", observations)
		self.assertNotIn("TooHigh", observations)
		self.assertEqual(
			errors,
			[(3, "temperature out of range"), (4, "temperature out of range")],
		)

	def test_calculated_statistics(self):
		observations = {
			"North": [
				(datetime.datetime(2026, 4, 20, 9, 0), 60.0),
				(datetime.datetime(2026, 4, 20, 10, 0), 70.0),
				(datetime.datetime(2026, 4, 20, 11, 0), 80.0),
			]
		}

		statistics = station_statistics(observations)

		self.assertEqual(statistics["North"]["min"], 60.0)
		self.assertEqual(statistics["North"]["max"], 80.0)
		self.assertEqual(statistics["North"]["mean"], 70.0)

	def test_sorted_output_and_one_decimal_format(self):
		statistics = {
			"Zulu": {"min": 5, "max": 15, "mean": 10},
			"Alpha": {"min": 1, "max": 3, "mean": 2},
		}
		filename = self.create_observation_file("")

		write_statistics(filename, statistics)

		with open(filename, "r") as file:
			self.assertEqual(
				file.read(),
				"Alpha,1.0,3.0,2.0\nZulu,5.0,15.0,10.0\n",
			)

	def test_missing_file_raises_file_access_error(self):
		with self.assertRaises(FileNotFoundError):
			read_observations("file_that_does_not_exist.txt")


if __name__ == "__main__":
	main()
