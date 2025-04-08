# AWS Image Resizer

This project demonstrates how to resize images using AWS Lambda and S3.

## Description

The AWS Image Resizer automatically resizes images when they are uploaded to an S3 bucket. The Lambda function resizes the images to a fixed width (300px) while maintaining their aspect ratio and saves them in the `output/` folder in S3.

## How It Works

1. When an image is uploaded to the `input/` folder in S3, it triggers an AWS Lambda function.
2. The Lambda function reads the image, resizes it, and stores the resized image in the `output/` folder in S3.
