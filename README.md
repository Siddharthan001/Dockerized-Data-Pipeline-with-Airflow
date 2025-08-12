**Assignment:** **Dockerized** **Data** **Pipeline** **with**
**Airﬂow:**

**Done** **by:** SIDDHARTHAN R

**Email:** siddharthanr25@gmail.com

**Overview:**

> This project is a scalable, automated data pipeline that crawls
> speciﬁed logistics/supply chain websites and ingests both raw and
> processed data into AWS S3.
>
> It also handles dynamic updates and stores the extracted data for
> further analysis. The pipeline is Dockerized for easy deployment and
> runs on scheduled intervals.

**Features:**

> Automated Web Crawling of multiple logistics/supply chain websites.
> Raw & Processed Data Storage in AWS S3.
>
> Data Processing & Cleaning to prepare structured output. Dockerized
> Environment for easy setup and deployment. Logging & Error Handling
> for reliability.
>
> Modular Architecture for easy scaling and updates.

**Project** **Structure:**

project-folder/

│

├── src/ \# Source code for crawler and processing scripts

│ ├── crawler.py

│ ├── processor.py

\# Main crawling logic

> \# Data cleaning and structuring

│ └── utils.py \# Helper functions

│

├── docker-compose.yml \# Docker conﬁguration

├── requirements.txt \# Python dependencies

├── conﬁg.yaml

├── README.md

\# Conﬁgurations for websites, AWS, etc.

> \# This documentation

└── Project Completed.

**Prerequisites:**

> Docker installed
>
> AWS Account (with S3 bucket ready)
>
> Python 3.9+ (if running locally without Docker) Valid AWS Credentials
> (Access Key & Secret Key)

**How** **to** **Run** **(Local):**

**1.** **Clone** **the** **Repository:**

Copy all the ﬁles in the project folder into vs code

cd project-folder

**2.** **Install** **Dependencies:**

pip install -r requirements.txt

**3.** **Set** **Environment** **Variables** **Create** **a** **.env**
**ﬁle** **and** **add:**

AWS_ACCESS_KEY_ID=your_key

AWS_SECRET_ACCESS_KEY=your_secret

AWS_REGION=your_region

S3_BUCKET_NAME=your_bucket

**4.** **Run** **the** **Pipeline:**

python src/crawler.py

> **How** **to** **Run** **with** **Docker:**

1\. Build the Image

docker build -t web-crawler .

2\. Run the Container

docker run --env-ﬁle .env web-crawler

3\. Using Docker Compose

docker-compose up --build

**Upload** **to** **AWS** **S3:**

The script automatically uploads processed ﬁles to your conﬁgured S3
bucket.

Check your bucket after execution:

aws s3 ls s3://your_bucket/

**Final** **Output:**

When the pipeline runs successfully:

You will see logs like:

**Extracting** **165** **s**

**Extracting** **168** **s**

**Data** **successfully** **uploaded** **to** **S3**

Data will be stored in your S3 bucket in structured folders.
