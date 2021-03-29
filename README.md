# webpage-article-extracter
A python API to extract the main article text from web pages independent of the html styles/structure.

### 1. Machine Setup to run apps (Dockers):

    - sudo apt-get update -y
    - sudo apt-get install docker.io

Docker setup:

    - sudo docker build -t web-extractor-image .
    - sudo docker run -d -p 80:80 web-extractor-image

### 2. Machine Setup to run apps (without Dockers):

    - pip3 install -r requirements.txt
    - uvicorn main:app --host 0.0.0.0 --port 80

### 3. Access swagger api page to test the API

    - open link: http://0.0.0.0/docs
    - Sample urls to test:
        * Tech blogs:
            https://aws.amazon.com/blogs/machine-learning/announcing-aws-media-intelligence-solutions/
        
        * News articles:
            https://arynews.tv/en/lahore-coronavirus-positivity-rate/
            https://edition.cnn.com/2021/03/24/tech/google-ai-ethics-reputation/index.html

        * Kid Stories: 
            https://americanliterature.com/childrens-stories/little-red-riding-hood

### 4. Optional Commands
Git reset commands (if needed):

	- git rm --cached filename
    - git rm -r --cached . && git add . && git commit -m ".gitignore is now working"

Remove dangling docker images:

    - sudo docker rmi $(sudo docker images -f "dangling=true" -q)
