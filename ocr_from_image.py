import io , os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\User\worktest\envtest\propane-ripsaw-333014-e2eacfee942d.json"

client = vision_v1.ImageAnnotatorClient()

#ไทย
img_url_th = 'https://www.goodtipit.com/wp-content/uploads/2020/05/Convert-photo-to-text.jpg'
image1 = vision_v1.types.Image()
image1.source.image_uri = img_url_th
response1 = client.text_detection(image=image1)
text1 =  response1.text_annotations
df1 = pd.DataFrame(columns=['locale1', 'description1'])
for text in text1:
    df1 = df1.append(
        dict(        
            locale1=text.locale,
            description1=text.description
        ),
        ignore_index=True
    )

#อังกฤษ
img_url_en = 'http://digitalnativestudios.com/textmeshpro/docs/rich-text/line-indent.png'
image2 = vision_v1.types.Image()
image2.source.image_uri = img_url_en
response2 = client.text_detection(image=image2)
text2=  response2.text_annotations
df2 = pd.DataFrame(columns=['locale2', 'description2'])
for text in text2:
    df2 = df2.append(
        dict(        
            locale2=text.locale,
            description2=text.description
        ),
        ignore_index=True
    )

'''
def detectText(img):
    with io.open(img , 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)
    response = client.text_detection(image=image)
    textsssss =  response.text_annotations

    df = pd.DataFrame(columns=['locale', 'description'])
    for text in textsssss:
        df = df.append(
            dict(        
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )
    return df


FILE_NAME = 'sample3.jpg'
FOLDER_PATH = r'D:/Coding/Python/vision_api/env/Image/Text'
print(detectText(os.path.join(FOLDER_PATH, FILE_NAME)))
'''

#print(df1['description1'][0] , df2['description2'][0])