from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
      "name": "github",
      "image": "githubLogo",
      "link": "https://github.com/cobbettn",
      "description": "My Github"
    },
    {
      "name": "linkedin",
      "image": "linkedinLogo",
      "link": "https://www.linkedin.com/in/nathan-cobbett/",
      "description": "LinkedIn"
    },
    {
      "name": "resume",
      "image": "resumeIcon",
      "link": "Resume",
      "description": "My Resume"
    },
    {
      "name": "bio",
      "image": "myFace",
      "description": "About me",
      "modalContent": [
        "I like to build things with web technologies. I started programming as a hobby in my downtime and it eventually turned into a career. Through my work as a software engineer I strive to create robust, accessible and performant applications that delight and empower users. I'm open to job opportunites where I can solve interesting problems and further expand my skill set as an engineer.", 
        "When I'm not on my computer I like spending time in the woods, retro gaming and bouldering. I also enjoy taking pictures as a hobby and help run a small photography business." 
     ]
    },
    {
      "name": "code",
      "image": "codeIcon",
      "link": "https://github.com/cobbettn/cobbettn.github.io",
      "description": "Code for this webpage"
    },
    {
      "name": "in progress",
      "image": "colorBars",
      "description": "in progress"
    },
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
