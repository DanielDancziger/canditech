Assumptions
- Question is unique per "Test"
- Questions can be reused for different companies
- For simplicity purposes all constants & tables definitions are in same file
- For simplicity all functions are in the same folder

Running in your AWS Account:
1) Configure AWS_CLI in your computer
2) git clone repository
3) run npm install serverless -g
3) Terminal in the repository folder run npm install
4) Install pipenv (pip3 install pipenv)
5) Terminal in repository folder run pipenv sync
6) Deploy solution to AWS run: sls deploy

Testing (Online Running Already):

Method: GET

Get Question: 
https://y610iy0hjl.execute-api.us-east-1.amazonaws.com/dev/questions/{questionId}

Get Question for Review:
https://y610iy0hjl.execute-api.us-east-1.amazonaws.com/dev/questions/{questionId}/review

Get Answer:
https://y610iy0hjl.execute-api.us-east-1.amazonaws.com/dev/answers/{answerId}

Get answer for candidate:
https://y610iy0hjl.execute-api.us-east-1.amazonaws.com/dev/candidate/{candidateId}/answers/question/{questionId}

Get Answers for candidate:
https://y610iy0hjl.execute-api.us-east-1.amazonaws.com/dev/candidate/{candidateId}/answers

Possible Candidates Id:
1, 2

Possible Questions Id:
1, 2, 3

Possible Answer Ids:
1, 2, 3, 4, 5, 6