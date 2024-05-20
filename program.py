import asyncio, os, argparse, sys
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, GetUserPhotosRequest, DeletePhotosRequest

load_dotenv()

api_id          = os.getenv('API_ID')
api_hash        = os.getenv('API_HASH')
client          = TelegramClient('anon', api_id, api_hash)
pictureDay      = os.getenv('PICTURE_DAY')
pictureNight    = os.getenv('PICTURE_NIGHT')

def processArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', help = 'Control the color-scheme. light or dark')
    parser.add_argument('--file', help = 'Provide a certain file. Overrides light and dark mode')
    return parser.parse_args()

def getPictureByColor(selectedColor):
    print('Color-mode:', selectedColor)
    
    if selectedColor == 'dark' or selectedColor == 'night':
        return pictureNight
    else:
        return pictureDay

def checkPicture(picturePath):
    return os.path.isfile(picturePath)

async def uploadPicture(picturePath):
    if checkPicture(picturePath):
        print('uploading file', picturePath)
        file = await client.upload_file(picturePath)
        result = await client(UploadProfilePhotoRequest(file=file))
        print('profile picture changed')
    else:
        print('image path not correct')

async def cleanupProfilePictures():
    photos = await client(GetUserPhotosRequest(user_id = 'me', offset = 0, max_id = 0, limit = 1))

    if photos.photos:
        latestPhoto = photos.photos[0]
        result = await client(DeletePhotosRequest(id = [latestPhoto]))

        if result:
            print('photo deleted')

async def main():
    color = 'light'
    args = processArguments()

    if args.color is not None:
        color = args.color.lower()

    if args.file is not None:
        pictureToUpload = args.file
    else:
        pictureToUpload = getPictureByColor(color)

    await cleanupProfilePictures()
    await uploadPicture(pictureToUpload)
    print('done')

with client:
    client.loop.run_until_complete(main())