from fastapi import FastAPI
import this
import codecs
app = FastAPI()

"""
@app.get("/")
def read_root():
  return codecs.encode(this.s, 'rot_13')
"""

wer='Hello world'
print(wer)