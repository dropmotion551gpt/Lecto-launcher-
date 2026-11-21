import base64
import io
import zipfile

data = "".join(open(f"part{i}.txt").read() for i in (1, 2, 3))
raw = base64.b64decode("".join(data.split()))
with zipfile.ZipFile(io.BytesIO(raw)) as zf:
    zf.extractall(".")
    print(f"Extracted {len(zf.namelist())} files OK")
    
