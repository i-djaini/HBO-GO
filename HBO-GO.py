#Encrypt by SC Ismail Djaini

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))