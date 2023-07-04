import shutil

shutil.make_archive("archive", "zip", "test")
shutil.unpack_archive("archive.zip")
