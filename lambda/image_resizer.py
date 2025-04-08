import boto3
import os
from PIL import Image
import io

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket name and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Ignore files that are not in the 'input/' folder
    if not key.startswith('input/'):
        print(f"Ignored file: {key}")
        return

    # Download the image from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    image_data = response['Body'].read()

    # Open the image using Pillow
    image = Image.open(io.BytesIO(image_data))

    # Resize image to width of 300px while keeping aspect ratio
    width = 300
    aspect_ratio = width / float(image.size[0])
    height = int(float(image.size[1]) * aspect_ratio)
    resized_image = image.resize((width, height))

    # Save the resized image to a temporary buffer
    buffer = io.BytesIO()
    resized_image.save(buffer, format="JPEG")
    buffer.seek(0)

    # Generate new filename and S3 key for the output
    filename = key.split('/')[-1]
    output_key = f"output/resized-{filename}"

    # Upload the resized image back to S3
    s3.put_object(Bucket=bucket, Key=output_key, Body=buffer, ContentType='image/jpeg')

    print(f"✅ Image processed and saved to: {output_key}")

