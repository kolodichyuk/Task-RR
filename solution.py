import sys, argparse, os, hashlib
from PIL import Image

class Item:
    def __init__(self, image_name, hash):
        self.image_name = image_name
        self.hash = hash

# entry point
def main(path):
    files = os.listdir(path)
    items = []
    for item in files:
        image = Image.open(path + '/' + item).resize((32, 32))
        md5_hash = hashlib.md5(image.tobytes()).hexdigest()
        items.append(Item(item, md5_hash))
    size = len(items)
    for i in range(0, size):
        for j in range(0, size):
            if items[i].hash == items[j].hash and i != j and items[i].hash != '0000':
                print(str(items[i].image_name) + ' ' + str(items[j].image_name))
                items[i].hash, items[j].hash = '0000', '0000'
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='path to data set')
    args = parser.parse_args()
    main(args.path)
