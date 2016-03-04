# aws-sns-lambda-demo


### Step 1: Create local files

Lambda function code is organized in the `./lambdas` directory. Each Lambda lives in its own subdirectory of that directory. The name of the subdirectory should be lowercase and use `_` to separate words. Example: `my_cool_lambda`.


### Step 2: Create SNS Topic

From the [SNS Console](https://console.aws.amazon.com/sns/v2/home) > Topics, click **Create new topic**. Enter a **Topic name**, using `-` to separate words. Example: `my-cool-topic`.


### Step 3: Create Lambda Function

From the [Lambda Console](https://console.aws.amazon.com/lambda/home), click **Create a Lambda function**. Select **Python 2.7** from the languages filter to limit results, then choose the **sns-message-python** blueprint. Click in the **SNS topic** field and select the topic created in the previous step, click **Next**. Give your function the same name you used in **Step 1**. Example: `my_cool_lambda`. Copy the starter code from the editor panel and paste it into a `main.py` file in your local Lambda directory (See **Step 1**). In the **Handler** field, change the value to `main.lambda_handler`. Choose the basic execution role in the **Role** dropdown. Click **Next**. Review information on the final screen and confirm.


### Step 4: Deploy with Fabric

After modifying the handler code locally, you can deploy with a Fabric command:
```
fab --set AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_KEY deploy_lambda:name_of_lambda
```
Replace `name_of_lambda` above with the name you used in **Step 1**. It is important that this name matches the subdirectory name in `./lambdas` because that's how the Fabric script finds the local files to zip and push to AWS.
