import os, argparse, json, base64
from PIL import Image
from io import BytesIO

def main(pth_src):
    bse, ext = os.path.splitext(os.path.basename(pth_src))
    print("cutting a json file that will contain a base64 string for the image {}{}".format(bse, ext))
    img = Image.open(pth_src)

    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = str(base64.b64encode(buffered.getvalue()).decode())

    pth_save = os.path.join(os.path.dirname(os.path.abspath(pth_src)), '{}.json'.format(bse))
    with open(pth_save, 'w') as fp:
        json.dump({'image':img_str}, fp)


if __name__ == '__main__' and __package__ is None:
    # ---- FEUTIL ---- #
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) # add grandparent folder to the module search path
    import _fresh_eyes_script_utilities as feu # import fresh eyes fe_util
    # ---- FEUTIL ---- #

    # ---- ARGPARSE ---- #
    parser = argparse.ArgumentParser()
    parser.add_argument('src_path', help="path at which to find a single source image.")
    args = parser.parse_args()
    # ---- ARGPARSE ---- #
    
    main(args.src_path)
