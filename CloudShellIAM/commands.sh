#!/bin/bash

aws iam list-users

aws iam create-user --user-name user1

#To create a login profile
aws iam create-login-profile --generate-cli-skeleton > createlogin.json #Edit the json and apply it
aws iam create-login-profile --cli-input-json file://createlogin.json

#Attach User Policy

aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name user1

#Create Access Key

aws iam create-access-key --user-name user1

#Create user

aws iam create-group --group-name Admins

aws iam add-user-to-group --user-name user1 --group-name Admins