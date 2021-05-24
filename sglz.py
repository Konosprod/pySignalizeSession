import json
import base64
import sys
import argparse


def load(file):
    jsono = ""

    with open(file, "r") as fd:
        es = base64.b64decode(fd.read())
        jsono = json.loads(es)

    return jsono

def extract(file):

    jsono = load(file)

    i = 1
    for music in jsono["musics"]:
        b64bytes = music["file"].encode("utf-8")

        with open("music" + str(i) + ".mp3", "wb") as out:
            ddata = base64.decodebytes(b64bytes)
            out.write(ddata)
        
        i += 1

    i = 1
    for music in jsono["midis"]:
        b64bytes = music["file"].encode("utf-8")

        with open("music" + str(i) + ".midi", "wb") as out:
            ddata = base64.decodebytes(b64bytes)
            out.write(ddata)
        
        i += 1


    for record in jsono["records"]:
        with open(record["name"] + ".mp3", "wb") as fd:
            b64bytes = record["voiceData"].encode("utf-8")
            ddata = base64.decodebytes(b64bytes)
            fd.write(ddata)

    with open("settings.json", "w") as fd:
        json.dump(jsono["settings"], fd)

    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sglz", help="File .sglz")
    parser.add_argument("-e", "--extract", action="store_true", help="Extract everything from the file")

    commands = parser.parse_args()

    if commands.extract:
        extract(commands.sglz)
    else:
        print(json.dumps(load(commands.sglz)))

    return

if __name__ == "__main__":
    main()
