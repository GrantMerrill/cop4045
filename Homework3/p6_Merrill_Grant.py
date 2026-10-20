# Grant Merrill --- Z23813057

class Entry:
    """A named entry that may belong to a parent entry."""

    def __init__(self, name: str, parent: "Entry | None" = None) -> None:
        """Initialize an entry with its name and optional parent."""
        self.name: str = name
        self._parent: Entry | None = parent

    def parent(self) -> "Entry | None":
        """Return this entry's parent, or ``None`` if it has none."""
        return self._parent

    def absolute_path(self) -> list["Entry"]:
        """Return this entry and its ancestors, ending with the root entry."""
        parent_entry = self.parent()
        if parent_entry is None:
            return [self]
        return [self, *parent_entry.absolute_path()]

    def size(self) -> int:
        """Return this entry's size in bytes."""
        raise NotImplementedError("Entry subclasses must implement size()")


class File(Entry):
    """A file entry with a non-negative size in bytes."""

    def __init__(
        self,
        name: str,
        bytes_used: int,
        parent: Entry | None = None,
    ) -> None:
        """Initialize a file with its name, byte size, and optional parent."""
        super().__init__(name, parent)
        if bytes_used < 0:
            raise ValueError("bytes_used must be non-negative")
        self.bytes_used: int = bytes_used

    def size(self) -> int:
        """Return the file's size in bytes."""
        return self.bytes_used


class Folder(Entry):
    """A folder entry containing files and other folders."""

    def __init__(self, name: str, parent: Entry | None = None) -> None:
        """Initialize a folder with its name, optional parent, and no children."""
        super().__init__(name, parent)
        self.__children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        """Add an entry to this folder's children."""
        self.__children.append(entry)

    def size(self) -> int:
        """Return the combined size of all children, including nested folders."""
        return sum(child.size() for child in self.__children)

    def children(self) -> tuple[Entry, ...]:
        """Return the folder's children as an immutable tuple."""
        return tuple(self.__children)


def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    """Find files at least ``minimum_size`` bytes within an entry.

    Args:
        entry: The file or folder to search. A file is tested directly; a
            folder's children are searched recursively, including nested folders.
        minimum_size: The inclusive minimum file size in bytes. A value of zero
            includes zero-byte files.

    Returns:
        A list of matching ``File`` objects. For a file, the result contains
        that file if its size meets the threshold; for a folder, it combines
        matches found among all descendants.
    """
    if isinstance(entry, File):
        return [entry] if entry.size() >= minimum_size else []

    if isinstance(entry, Folder):
        matches: list[File] = []
        for child in entry.children():
            matches.extend(find_large_files(child, minimum_size))
        return matches

    return []


def demonstrate_hierarchy() -> None:
    """Build a nested folder hierarchy and demonstrate size and file search."""
    root = Folder("root")
    subfolder = Folder("subfolder", root)
    nested_folder = Folder("nested", subfolder)

    root_file = File("root.txt", 40, root)
    subfolder_file = File("subfolder.txt", 90, subfolder)
    nested_small_file = File("nested-small.txt", 70, nested_folder)
    nested_large_file = File("nested-large.txt", 160, nested_folder)

    root.add(root_file)
    root.add(subfolder)
    subfolder.add(subfolder_file)
    subfolder.add(nested_folder)
    nested_folder.add(nested_small_file)
    nested_folder.add(nested_large_file)

    root_file_path = root_file.absolute_path()
    subfolder_file_path = subfolder_file.absolute_path()
    nested_large_file_path = nested_large_file.absolute_path()

    assert root_file_path == [root_file, root]
    assert subfolder_file_path == [subfolder_file, subfolder, root]
    assert nested_large_file_path == [nested_large_file, nested_folder, subfolder, root]

    print("Absolute paths:")
    print([entry.name for entry in root_file_path])
    print([entry.name for entry in subfolder_file_path])
    print([entry.name for entry in nested_large_file_path])

    total_size = root.size()
    assert total_size == 360
    print(f"Total size: {total_size} bytes")

    medium_and_larger = find_large_files(root, 75)
    assert medium_and_larger == [subfolder_file, nested_large_file]
    print("Files at least 75 bytes:")
    for file_entry in medium_and_larger:
        print(f"{file_entry.name}: {file_entry.size()} bytes")

    large_only = find_large_files(root, 150)
    assert large_only == [nested_large_file]
    print("Files at least 150 bytes:")
    for file_entry in large_only:
        print(f"{file_entry.name}: {file_entry.size()} bytes")


import unittest

class EntryTests(unittest.TestCase):
    """Tests for entry paths and recursive large-file discovery."""

    def test_absolute_path_from_root(self) -> None:
        """A root entry's absolute path contains only itself."""
        root = Folder("root")

        self.assertEqual(root.absolute_path(), [root])

    def test_absolute_path_from_nested_file(self) -> None:
        """A nested file's path is ordered from itself to the root."""
        root = Folder("root")
        child_folder = Folder("child", root)
        file_entry = File("notes.txt", 12, child_folder)

        self.assertEqual(file_entry.absolute_path(), [file_entry, child_folder, root])

    def test_finds_large_file_directly(self) -> None:
        """A file is returned when its size meets the inclusive threshold."""
        file_entry = File("large.bin", 100)

        self.assertEqual(find_large_files(file_entry, 100), [file_entry])
        self.assertEqual(find_large_files(file_entry, 101), [])

    def test_finds_files_in_nested_folders(self) -> None:
        """Matching files in all descendant folders are returned."""
        root = Folder("root")
        nested = Folder("nested", root)
        first = File("first.bin", 50)
        second = File("second.bin", 150)
        nested.add(first)
        root.add(nested)
        root.add(second)

        self.assertEqual(find_large_files(root, 100), [second])

    def test_zero_threshold_includes_zero_byte_files(self) -> None:
        """A zero threshold includes zero-byte files as well as larger files."""
        root = Folder("root")
        empty_file = File("empty.txt", 0)
        nonempty_file = File("data.bin", 1)
        root.add(empty_file)
        root.add(nonempty_file)

        self.assertEqual(find_large_files(root, 0), [empty_file, nonempty_file])


if __name__ == "__main__":
    demonstrate_hierarchy()
    unittest.main()
