#Encrypt by SC Ismail Djaini

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))