# api-resume-reviewer
API for reviewing resumes via gen ai

## running through docker
1. Make sure you have the docker daemon running
2. run `docker compose up --build`

## deployed to fly.io
1. `fly deploy` - currently in person account <jjustin634@gmail.com>

## type annotation check
1. `mypy .`

## code linting, formatting, and sorting imports
1. `ruff .`
    - For sorting then use `ruff . --fix`
2. `ruff format`

# Example execution

API `api/resume/review` as POST
- Upload resume
- Specify company name you are applying for
- Specify the title you are applying for

## Example response with recommendations on resume updates
#### e.g. title=Software Engineer, company=Carvana

```json
{
  "filename": "jj_resume.pdf",
  "original_resume": {
    "Summary": "Experienced Full-Stack Software Engineer driven by a passion for innovation and the application of emerging tech and AI. Committed to building solutions that improve people's lives and enhancing my technical skills daily. Now seeking a progressive role to continue creating impactful and transformative software solutions.",
    "Work History": {
      "2019-06 - Current": {
        "Title": "Data Engineer",
        "Company": "Travelers Insurance, Saint Paul, MN",
        "Responsibilities": [
          "Developed MapReduce paradigm with AWS Lambda that improves performance and cost by 100% for data quality checks.",
          "Led Front end development of a Proactive Monitoring MVP using React.",
          "Developed patterns using GraphQL within AWS, wrote architecture newsletter that was distributed to over 500 engineers.",
          "Led the development of numerous APIs for API Strategy initiative that allows teams and engineers to ingest/consume data by APIs within S3 data layers. Enables metadata capture to have a compressive view of data movement and lineage.",
          "Was given the opportunity to be the SWE Lead for shared innovation.",
          "Mentored various employees and managed summer interns directly in 2022-2023 summers.",
          "Have held 6 different titles in my journey at Travelers thus far in 4 years."
        ]
      }
    },
    "Education": {
      "2018-06 - 2020-12": {
        "Degree": "Bachelor of Science: Computer Science",
        "Institution": "Concordia University, St. Paul - Saint Paul, MN"
      },
      "2017-08 - 2018-05": {
        "Degree": "Associate of Science: Computer Science",
        "Institution": "Century College - White Bear Lake, MN"
      }
    },
    "Contact": {
      "Location": "Saint Paul, MN",
      "E-mail": "jjustin634@gmail.com",
      "Phone": "",
      "LinkedIn": "https://www.linkedin.com/in/justin-johnson-413a931",
      "GitHub": "https://github.com/justinjohnson-dev"
    },
    "Certifications": [
      {
        "Name": "AWS Certified Developer",
        "ID": "71DLSYC2QIQ41E5F"
      },
      {
        "Name": "AWS Solutions Architect",
        "ID": "TMEJYCD15NV41Q9B"
      },
      {
        "Name": "AWS Data Analytics",
        "ID": "RTXR9151YMBQ15C4"
      },
      {
        "Name": "AWS Cloud Practitioner",
        "ID": "1C2T8K2J32VQQ15Y"
      },
      {
        "Name": "Systems Design",
        "ID": "c07263ef29"
      }
    ],
    "References": "Available upon request",
    "Projects": [
      {
        "Date": "2022-12",
        "Name": "Open AI Twitter Bot",
        "Description": "Twitter bot that uses Open AI text-davinci-003 model that finds a random noun and tweets an explanation of the words with a comedic touch!",
        "Visit Project": "https://twitter.com/jj_devbot_",
        "Code Base": "https://github.com/justinjohnson-dev/openai_twitter_bot",
        "Skills": [
          "GPT-3",
          "Twitter API",
          "EC2",
          "Python",
          "Node.js",
          "Express.js"
        ]
      },
      {
        "Date": "2023-01 - 2023-06",
        "Name": "Track Daily Expenses",
        "Description": "Application that allows users to track every incoming and outgoing expense. Currently a Next.js application deployed to Vercel that is mobile styled only. Auth0 is used for authentication, MongoDB cluster for database. A lot of features that show breakdowns of all your expenses year-to-date, month-month, graphs to show spending categories. Information about how much you are spending/saving in a given month and year to date.",
        "Visit Project": "https://github.com/justinjohnson-dev/track-daily-expenses",
        "Skills": [
          "Next.js",
          "Prisma",
          "Vercel",
          "TypeScript",
          "React.js",
          "MongoDB"
        ]
      },
      {
        "Date": "2021-06 - 2022-12",
        "Name": "Birthday Reminder",
        "Description": "Full-Stack application that allows users to opt into text messages to receive texts when a family/friend has a birthday. React frontend that needs to be rebuilt in Next.js Express server using node-cron to run every morning at 8AM to check for users’ birthdays, if a birthday is found, twilio is used to text that individual.",
        "Visit Project": "https://github.com/justinjohnson-dev/birthday-reminder-twilio-sms",
        "Skills": [
          "Express.js",
          "mongoose",
          "Heroku",
          "JavaScript",
          "React.js",
          "MongoDB"
        ]
      }
    ],
    "Skills": {
      "Languages": [
        "JavaScript",
        "Python"
      ],
      "Frameworks / Libraries": [
        "React",
        "Next.js",
        "Express"
      ],
      "Data Layer": [
        "SQL",
        "NoSQL"
      ]
    },
    "desired_job_title": "Software Engineer",
    "desired_company_name": "AWS Web Services"
  },
  "resume_recommendations": {
    "Summary": {
      "recommended_change": "Tailor the summary to align more closely with the desired role at AWS Web Services. Highlight specific skills and experiences that are relevant to the job description.",
      "change_made": "Experienced Full-Stack Software Engineer with a strong background in AWS technologies and a passion for innovation and AI. Committed to building solutions that improve people's lives and enhancing my technical skills daily. Now seeking a role at AWS Web Services to continue creating impactful and transformative software solutions."
    },
    "Work History": {
      "2019-06 - Current": {
        "recommended_change": "Clarify the progression of roles within the company to show career growth. Highlight specific achievements and technologies used that are relevant to the desired role.",
        "change_made": {
          "Title": "Senior Data Engineer",
          "Company": "Travelers Insurance, Saint Paul, MN",
          "Responsibilities": [
            "Developed MapReduce paradigm with AWS Lambda that improved performance and cost by 100% for data quality checks.",
            "Led front-end development of a Proactive Monitoring MVP using React.",
            "Developed patterns using GraphQL within AWS and wrote an architecture newsletter distributed to over 500 engineers.",
            "Led the development of numerous APIs for the API Strategy initiative, enabling teams to ingest/consume data within S3 data layers and capture metadata for comprehensive data movement and lineage views.",
            "Served as the SWE Lead for shared innovation projects.",
            "Mentored various employees and managed summer interns directly in 2022-2023.",
            "Held 6 different titles over 4 years, demonstrating career growth and versatility."
          ]
        }
      }
    },
    "Projects": {
      "2022-12": {
        "recommended_change": "Emphasize the use of AWS technologies in the project description to align with the desired role.",
        "change_made": {
          "Description": "Twitter bot that uses Open AI text-davinci-003 model to find a random noun and tweet an explanation with a comedic touch. Deployed on AWS EC2 for scalability and reliability.",
          "Skills": [
            "GPT-3",
            "Twitter API",
            "AWS EC2",
            "Python",
            "Node.js",
            "Express.js"
          ]
        }
      },
      "2023-01 - 2023-06": {
        "recommended_change": "Highlight the use of AWS services if applicable, or emphasize the scalability and deployment aspects.",
        "change_made": {
          "Description": "Application that allows users to track every incoming and outgoing expense. Deployed on Vercel with a mobile-first design. Uses Auth0 for authentication and a MongoDB cluster for the database. Features include year-to-date and month-to-month expense breakdowns, spending category graphs, and savings insights.",
          "Skills": [
            "Next.js",
            "Prisma",
            "Vercel",
            "TypeScript",
            "React.js",
            "MongoDB"
          ]
        }
      },
      "2021-06 - 2022-12": {
        "recommended_change": "Mention any AWS services used or emphasize the deployment and scalability aspects.",
        "change_made": {
          "Description": "Full-Stack application that allows users to opt into text messages for birthday reminders. React frontend with plans to rebuild in Next.js. Uses an Express server with node-cron to check for birthdays daily at 8 AM, and Twilio for sending text messages. Deployed on Heroku.",
          "Skills": [
            "Express.js",
            "mongoose",
            "Heroku",
            "JavaScript",
            "React.js",
            "MongoDB"
          ]
        }
      }
    },
    "Skills": {
      "recommended_change": "Expand the skills section to include more AWS-specific technologies and tools relevant to the desired role.",
      "change_made": {
        "Languages": [
          "JavaScript",
          "Python"
        ],
        "Frameworks / Libraries": [
          "React",
          "Next.js",
          "Express"
        ],
        "Data Layer": [
          "SQL",
          "NoSQL"
        ],
        "Cloud Services": [
          "AWS Lambda",
          "AWS EC2",
          "AWS S3",
          "AWS CloudFormation"
        ],
        "Other": [
          "GraphQL",
          "API Development",
          "Mentorship"
        ]
      }
    },
    "overview": "The summary was tailored to align with the desired role at AWS Web Services. The work history was clarified to show career progression and relevant achievements. Project descriptions were updated to emphasize the use of AWS technologies and deployment aspects. The skills section was expanded to include more AWS-specific technologies and tools."
  }
}
```

### current issues with responses
1. Although specified in PROMPT, sometimes the model with recommend changes that are potentially non-ethical. Such as changing my job title to `Senior Data Engineer` instead of `Data Engineer` (which was original title on resume).
2. Needs more indepth overview section. Currently just takes the company you want to work for and says "add more xxx specific services"

### next example is a response from a non tech company for application.
#### e.g. title=Software Engineer, company=Carvana

```json
{
  "filename": "jj_resume.pdf",
  "original_resume": {
    "Summary": "Experienced Full-Stack Software Engineer driven by a passion for innovation and the application of emerging tech and AI. Committed to building solutions that improve people's lives and enhancing my technical skills daily. Now seeking a progressive role to continue creating impactful and transformative software solutions.",
    "Work History": {
      "2019-06 - Current": {
        "Title": "Data Engineer",
        "Company": "Travelers Insurance, Saint Paul, MN",
        "Responsibilities": [
          "Developed MapReduce paradigm with AWS Lambda that improves performance and cost by 100% for data quality checks.",
          "Led Front end development of a Proactive Monitoring MVP using React.",
          "Developed patterns using GraphQL within AWS, wrote architecture newsletter that was distributed to over 500 engineers.",
          "Led the development of numerous APIs for API Strategy initiative that allows teams and engineers to ingest/consume data by APIs within S3 data layers. Enables metadata capture to have a compressive view of data movement and lineage.",
          "Was given the opportunity to be the SWE Lead for shared innovation.",
          "Mentored various employees and managed summer interns directly in 2022-2023 summers.",
          "Have held 6 different titles in my journey at Travelers thus far in 4 years."
        ]
      }
    },
    "Education": {
      "2018-06 - 2020-12": {
        "Degree": "Bachelor of Science: Computer Science",
        "Institution": "Concordia University, St. Paul - Saint Paul, MN"
      },
      "2017-08 - 2018-05": {
        "Degree": "Associate of Science: Computer Science",
        "Institution": "Century College - White Bear Lake, MN"
      }
    },
    "Contact": {
      "Location": "Saint Paul, MN",
      "E-mail": "jjustin634@gmail.com",
      "Phone": "",
      "LinkedIn": "https://www.linkedin.com/in/justin-johnson-413a931",
      "GitHub": "https://github.com/justinjohnson-dev"
    },
    "Certifications": [
      "AWS Certified Developer - ID: 71DLSYC2QIQ41E5F",
      "AWS Solutions Architect - ID: TMEJYCD15NV41Q9B",
      "AWS Data Analytics - ID: RTXR9151YMBQ15C4",
      "AWS Cloud Practitioner - ID: 1C2T8K2J32VQQ15Y",
      "Systems Design - ID: c07263ef29"
    ],
    "References": "Available upon request",
    "Projects": [
      {
        "Title": "Open AI Twitter Bot",
        "Date": "2022-12",
        "Description": "Twitter bot that uses Open AI text-davinci-003 model that finds a random noun and tweets an explanation of the words with a comedic touch!",
        "Links": {
          "Visit Project": "https://twitter.com/jj_devbot_",
          "Code Base": "https://github.com/justinjohnson-dev/openai_twitter_bot"
        },
        "Skills": [
          "GPT-3",
          "Twitter API",
          "EC2",
          "Python",
          "Node.js",
          "Express.js"
        ]
      },
      {
        "Title": "Track Daily Expenses",
        "Date": "2023-01 - 2023-06",
        "Description": "Application that allows users to track every incoming and outgoing expense. Currently a Next.js application deployed to Vercel that is mobile styled only. Auth0 is used for authentication, MongoDB cluster for database. A lot of features that show breakdowns of all your expenses year-to-date, month-month, graphs to show spending categories. Information about how much you are spending/saving in a given month and year to date.",
        "Links": {
          "Visit Project": "https://github.com/justinjohnson-dev/track-daily-expenses"
        },
        "Skills": [
          "Next.js",
          "Prisma",
          "Vercel",
          "TypeScript",
          "React.js",
          "MongoDB"
        ]
      },
      {
        "Title": "Birthday Reminder",
        "Date": "2021-06 - 2022-12",
        "Description": "Full-Stack application that allows users to opt into text messages to receive texts when a family/friend has a birthday. React frontend that needs to be rebuilt in Next.js Express server using node-cron to run every morning at 8AM to check for users’ birthdays, if a birthday is found, twilio is used to text that individual.",
        "Links": {
          "Visit Project": "https://github.com/justinjohnson-dev/birthday-reminder-twilio-sms"
        },
        "Skills": [
          "Express.js",
          "mongoose",
          "Heroku",
          "JavaScript",
          "React.js",
          "MongoDB"
        ]
      }
    ],
    "Skills": {
      "Languages": [
        "JavaScript",
        "Python"
      ],
      "Frameworks / Libraries": [
        "React",
        "Next.js",
        "Express"
      ],
      "Data Layer": [
        "SQL",
        "NoSQL"
      ]
    },
    "desired_job_title": "Software Engineer",
    "desired_company_name": "Carvana"
  },
  "resume_recommendations": {
    "Summary": {
      "recommended_change": "The summary is well-written but could be more tailored to the desired role at Carvana. Highlight specific skills and experiences that align with Carvana's needs, such as your experience with APIs, cloud technologies, and full-stack development.",
      "change_made": "Experienced Full-Stack Software Engineer driven by a passion for innovation and the application of emerging tech and AI. Committed to building solutions that improve people's lives and enhancing my technical skills daily. Now seeking a progressive role at Carvana to continue creating impactful and transformative software solutions, leveraging my expertise in APIs, cloud technologies, and full-stack development."
    },
    "Work History": {
      "2019-06 - Current": {
        "recommended_change": "Clarify the impact of your work and quantify achievements where possible. Also, specify the different titles held to show career progression.",
        "change_made": {
          "Title": "Data Engineer",
          "Company": "Travelers Insurance, Saint Paul, MN",
          "Responsibilities": [
            "Developed MapReduce paradigm with AWS Lambda that improved performance and reduced costs by 100% for data quality checks.",
            "Led front-end development of a Proactive Monitoring MVP using React, resulting in a more efficient monitoring process.",
            "Developed patterns using GraphQL within AWS and authored an architecture newsletter distributed to over 500 engineers.",
            "Led the development of numerous APIs for the API Strategy initiative, enabling teams to ingest/consume data within S3 data layers and capture metadata for comprehensive data movement and lineage views.",
            "Served as the SWE Lead for shared innovation, driving forward-thinking projects.",
            "Mentored various employees and managed summer interns directly in 2022-2023 summers, fostering a collaborative and educational environment.",
            "Held 6 different titles in my journey at Travelers thus far in 4 years, demonstrating career progression and adaptability."
          ]
        }
      }
    },
    "Education": {
      "2018-06 - 2020-12": {
        "recommended_change": "Include any relevant coursework or projects that align with the desired role at Carvana.",
        "change_made": {
          "Degree": "Bachelor of Science: Computer Science",
          "Institution": "Concordia University, St. Paul - Saint Paul, MN",
          "Relevant Coursework": [
            "Data Structures",
            "Algorithms",
            "Database Management Systems",
            "Software Engineering"
          ]
        }
      },
      "2017-08 - 2018-05": {
        "recommended_change": "Include any relevant coursework or projects that align with the desired role at Carvana.",
        "change_made": {
          "Degree": "Associate of Science: Computer Science",
          "Institution": "Century College - White Bear Lake, MN",
          "Relevant Coursework": [
            "Introduction to Programming",
            "Web Development",
            "Computer Systems"
          ]
        }
      }
    },
    "Projects": {
      "Open AI Twitter Bot": {
        "recommended_change": "Highlight the impact or reception of the project if available.",
        "change_made": {
          "Title": "Open AI Twitter Bot",
          "Date": "2022-12",
          "Description": "Twitter bot that uses Open AI text-davinci-003 model to find a random noun and tweet an explanation with a comedic touch. Gained over 500 followers within the first month.",
          "Links": {
            "Visit Project": "https://twitter.com/jj_devbot_",
            "Code Base": "https://github.com/justinjohnson-dev/openai_twitter_bot"
          },
          "Skills": [
            "GPT-3",
            "Twitter API",
            "EC2",
            "Python",
            "Node.js",
            "Express.js"
          ]
        }
      },
      "Track Daily Expenses": {
        "recommended_change": "Highlight the impact or reception of the project if available.",
        "change_made": {
          "Title": "Track Daily Expenses",
          "Date": "2023-01 - 2023-06",
          "Description": "Application that allows users to track every incoming and outgoing expense. Currently a Next.js application deployed to Vercel that is mobile styled only. Auth0 is used for authentication, MongoDB cluster for database. Features include breakdowns of all expenses year-to-date, month-to-month, graphs showing spending categories, and information on spending/saving in a given month and year-to-date. Used by over 100 users within the first three months.",
          "Links": {
            "Visit Project": "https://github.com/justinjohnson-dev/track-daily-expenses"
          },
          "Skills": [
            "Next.js",
            "Prisma",
            "Vercel",
            "TypeScript",
            "React.js",
            "MongoDB"
          ]
        }
      },
      "Birthday Reminder": {
        "recommended_change": "Highlight the impact or reception of the project if available.",
        "change_made": {
          "Title": "Birthday Reminder",
          "Date": "2021-06 - 2022-12",
          "Description": "Full-Stack application that allows users to opt into text messages to receive texts when a family/friend has a birthday. React frontend that needs to be rebuilt in Next.js. Express server using node-cron to run every morning at 8AM to check for users’ birthdays, if a birthday is found, Twilio is used to text that individual. Used by over 200 users, ensuring no birthdays are missed.",
          "Links": {
            "Visit Project": "https://github.com/justinjohnson-dev/birthday-reminder-twilio-sms"
          },
          "Skills": [
            "Express.js",
            "mongoose",
            "Heroku",
            "JavaScript",
            "React.js",
            "MongoDB"
          ]
        }
      }
    },
    "Skills": {
      "recommended_change": "Expand the skills section to include more specific technologies and tools relevant to the desired role at Carvana.",
      "change_made": {
        "Languages": [
          "JavaScript",
          "Python",
          "TypeScript"
        ],
        "Frameworks / Libraries": [
          "React",
          "Next.js",
          "Express",
          "Node.js"
        ],
        "Data Layer": [
          "SQL",
          "NoSQL",
          "MongoDB"
        ],
        "Cloud Technologies": [
          "AWS",
          "Vercel"
        ],
        "APIs": [
          "GraphQL",
          "REST"
        ]
      }
    },
    "overview": "The summary was tailored to align more closely with the desired role at Carvana. The work history section was enhanced to clarify the impact of the candidate's work and quantify achievements. Relevant coursework was added to the education section. The projects section was updated to highlight the impact or reception of each project. The skills section was expanded to include more specific technologies and tools relevant to the desired role."
  }
}
```

### analysis of response for Carvana
1. Does a better job trying to recommend improvements that are not just tech specific

#### thoughts on improvements
1. We could have the model do some research on the company the applicant wants to apply to
2. We could research sites like glassdoor to get interview experience that could potentially help and be reflected on individuals resume
3. Could build langchain agent specific for this type of task that can run a chain of requests.


## finally, e.g. of a tech resume application for a non-tech position
#### e.g. title=Warehouse Custodian / Janitor, company=Uline

```json
{
  "filename": "jj_resume.pdf",
  "original_resume": {
    "Summary": "Experienced Full-Stack Software Engineer driven by a passion for innovation and the application of emerging tech and AI. Committed to building solutions that improve people's lives and enhancing my technical skills daily. Now seeking a progressive role to continue creating impactful and transformative software solutions.",
    "Work History": {
      "2019-06 - Current": {
        "Title": "Data Engineer",
        "Company": "Travelers Insurance, Saint Paul, MN",
        "Responsibilities": [
          "Developed MapReduce paradigm with AWS Lambda that improves performance and cost by 100% for data quality checks.",
          "Led Front end development of a Proactive Monitoring MVP using React.",
          "Developed patterns using GraphQL within AWS, wrote architecture newsletter that was distributed to over 500 engineers.",
          "Led the development of numerous APIs for API Strategy initiative that allows teams and engineers to ingest/consume data by APIs within S3 data layers. Enables metadata capture to have a compressive view of data movement and lineage.",
          "Was given the opportunity to be the SWE Lead for shared innovation.",
          "Mentored various employees and managed summer interns directly in 2022-2023 summers.",
          "Have held 6 different titles in my journey at Travelers thus far in 4 years."
        ]
      }
    },
    "Education": {
      "2018-06 - 2020-12": {
        "Degree": "Bachelor of Science: Computer Science",
        "Institution": "Concordia University, St. Paul - Saint Paul, MN"
      },
      "2017-08 - 2018-05": {
        "Degree": "Associate of Science: Computer Science",
        "Institution": "Century College - White Bear Lake, MN"
      }
    },
    "Contact": {
      "Location": "Saint Paul, MN",
      "E-mail": "jjustin634@gmail.com",
      "Phone": "",
      "LinkedIn": "https://www.linkedin.com/in/justin-johnson-413a931",
      "GitHub": "https://github.com/justinjohnson-dev"
    },
    "Certifications": [
      {
        "Name": "AWS Certified Developer",
        "ID": "71DLSYC2QIQ41E5F"
      },
      {
        "Name": "AWS Solutions Architect",
        "ID": "TMEJYCD15NV41Q9B"
      },
      {
        "Name": "AWS Data Analytics",
        "ID": "RTXR9151YMBQ15C4"
      },
      {
        "Name": "AWS Cloud Practitioner",
        "ID": "1C2T8K2J32VQQ15Y"
      },
      {
        "Name": "Systems Design",
        "ID": "c07263ef29"
      }
    ],
    "References": "Available upon request",
    "Projects": [
      {
        "Name": "Open AI Twitter Bot",
        "Date": "2022-12 – 2022-12",
        "Description": "Twitter bot that uses Open AI text-davinci-003 model that finds a random noun and tweets an explanation of the words with a comedic touch!",
        "Links": {
          "Visit Project": "https://twitter.com/jj_devbot_",
          "Code Base": "https://github.com/justinjohnson-dev/openai_twitter_bot"
        },
        "Skills": [
          "GPT-3",
          "Twitter API",
          "EC2",
          "Python",
          "Node.js",
          "Express.js"
        ]
      },
      {
        "Name": "Track Daily Expenses",
        "Date": "2023-01 – 2023-06",
        "Description": "Application that allows users to track every incoming and outgoing expense. Currently a Next.js application deployed to Vercel that is mobile styled only. Auth0 is used for authentication, MongoDB cluster for database. A lot of features that show breakdowns of all your expenses year-to-date, month-month, graphs to show spending categories. Information about how much you are spending/saving in a given month and year to date.",
        "Links": {
          "Visit Project": "https://github.com/justinjohnson-dev/track-daily-expenses"
        },
        "Skills": [
          "Next.js",
          "Prisma",
          "Vercel",
          "TypeScript",
          "React.js",
          "MongoDB"
        ]
      },
      {
        "Name": "Birthday Reminder",
        "Description": "Full-Stack application that allows users to opt into text messages to receive texts when a family/friend has a birthday. React frontend that needs to be rebuilt in Next.js Express server using node-cron to run every morning at 8AM to check for users’ birthdays, if a birthday is found, twilio is used to text that individual.",
        "Links": {
          "Visit Project": "https://github.com/justinjohnson-dev/birthday-reminder-twilio-sms"
        },
        "Skills": [
          "Express.js",
          "mongoose",
          "Heroku",
          "JavaScript",
          "React.js",
          "MongoDB"
        ]
      }
    ],
    "Skills": {
      "Languages": [
        "JavaScript",
        "Python"
      ],
      "Frameworks / Libraries": [
        "React",
        "Next.js",
        "Express"
      ],
      "Data Layer": [
        "SQL",
        "NoSQL"
      ]
    },
    "desired_job_title": "Warehouse Custodian / Janitor",
    "desired_company_name": "Uline"
  },
  "resume_recommendations": {
    "Summary": {
      "recommended_change": "Tailor the summary to align with the desired job title of Warehouse Custodian / Janitor. Highlight relevant skills such as attention to detail, reliability, and physical stamina.",
      "change_made": "Experienced professional driven by a passion for maintaining clean and organized environments. Committed to ensuring safety and cleanliness in the workplace. Now seeking a role as a Warehouse Custodian / Janitor to contribute to a well-maintained and efficient warehouse."
    },
    "Work History": {
      "2019-06 - Current": {
        "recommended_change": "Adjust the job title and responsibilities to reflect transferable skills relevant to a custodian/janitor role. Emphasize organizational skills, attention to detail, and any physical tasks performed.",
        "change_made": {
          "Title": "Data Engineer",
          "Company": "Travelers Insurance, Saint Paul, MN",
          "Responsibilities": [
            "Developed efficient processes to ensure data quality and integrity.",
            "Led the organization and maintenance of data storage systems.",
            "Implemented monitoring systems to ensure operational efficiency.",
            "Developed and maintained APIs to streamline data access and management.",
            "Led a team in maintaining a clean and organized work environment.",
            "Mentored team members on best practices for maintaining data systems.",
            "Held multiple roles, demonstrating adaptability and a strong work ethic."
          ]
        }
      }
    },
    "Projects": {
      "recommended_change": "Remove or minimize the technical details of the projects and instead focus on any organizational, maintenance, or physical tasks involved.",
      "change_made": [
        {
          "Name": "Open AI Twitter Bot",
          "Date": "2022-12 – 2022-12",
          "Description": "Developed a project that required meticulous attention to detail and consistent monitoring to ensure proper functionality.",
          "Links": {},
          "Skills": [
            "Attention to Detail",
            "Consistency",
            "Monitoring"
          ]
        },
        {
          "Name": "Track Daily Expenses",
          "Date": "2023-01 – 2023-06",
          "Description": "Created an application that required thorough organization and tracking of data, demonstrating strong organizational skills.",
          "Links": {},
          "Skills": [
            "Organization",
            "Data Tracking",
            "Attention to Detail"
          ]
        },
        {
          "Name": "Birthday Reminder",
          "Description": "Developed a system that required regular maintenance and monitoring to ensure timely notifications, showcasing reliability and consistency.",
          "Links": {},
          "Skills": [
            "Maintenance",
            "Monitoring",
            "Reliability"
          ]
        }
      ]
    },
    "Skills": {
      "recommended_change": "Replace technical skills with skills relevant to a custodian/janitor role such as attention to detail, reliability, physical stamina, and organizational skills.",
      "change_made": {
        "Languages": [
          "Attention to Detail",
          "Reliability"
        ],
        "Frameworks / Libraries": [
          "Physical Stamina",
          "Organizational Skills"
        ],
        "Data Layer": [
          "Time Management",
          "Safety Awareness"
        ]
      }
    },
    "overview": "The resume has been tailored to align with the desired job title of Warehouse Custodian / Janitor at Uline. The summary, work history, projects, and skills sections have been adjusted to emphasize relevant skills such as attention to detail, reliability, physical stamina, and organizational skills. Technical details have been minimized to focus on transferable skills applicable to the custodian/janitor role."
  }
}
```

## analysis 
1. this completely breaks the current resume
  - for skills section on my tech resume it recommended words that someone from Uline management would want to see but completely in the wrong context.
  - e.g. ```json 
    "Skills": {
      "recommended_change": "Replace technical skills with skills relevant to a custodian/janitor role such as attention to detail, reliability, physical stamina, and organizational skills.",
      "change_made": {
        "Languages": [
          "Attention to Detail",
          "Reliability"
        ],
        "Frameworks / Libraries": [
          "Physical Stamina",
          "Organizational Skills"
        ],
        "Data Layer": [
          "Time Management",
          "Safety Awareness"
        ]
      }
    }```
    - languages here on my tech resume are programming languages... you get the idea of the rest. 

## improvements
1. could add a field to identify if user is applying for a different/new role than they are currently in.
2. add a validation layer to ensure that if the resume is completely different than the desired job, that the structure of the recommendations change with it.
