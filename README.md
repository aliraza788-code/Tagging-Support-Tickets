#  Support Ticket Auto Tagging (Zero-Shot Classification)

##  Objective
This project automatically classifies support tickets into relevant categories using a **Zero-Shot Learning approach** with Large Language Models (LLMs).

The system predicts the **Top 3 most relevant tags** for each support ticket without any prior training.

---

##  Features
- ✅ Zero-shot classification (No training required)
- ✅ Multi-class prediction
- ✅ Top 3 tag ranking
- ✅ Real-time user input
- ✅ Confidence score for each tag

---

##  How It Works
The project uses the **facebook/bart-large-mnli** model from HuggingFace.

- The model is given:
  - A support ticket (input text)
  - A list of predefined labels (categories)
- It then predicts the most relevant labels using natural language understanding.

---

##  Categories (Labels)

- Billing Issue  
- Technical Support  
- Account Access  
- Refund Request  
- Bug Report  
- Payment Problem  
- Login Issue  

---

##  Project Structure


support-ticket-zero-shot/
│
├── app.py # Main application (run this)
├── labels.py # List of categories
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

##  Installation

###  Clone or download the project

```bash
git clone <your-repo-link>
cd support-ticket-zero-shot
Install dependencies
pip install -r requirements.txt
 Usage

Run the application:

python app.py
 Example Interaction
 Support Ticket Classifier (Zero-Shot)

Enter ticket: I can't login to my account

Top 3 Tags:
Login Issue (0.88)
Account Access (0.82)
Technical Support (0.60)

Type exit to quit the program.

 Output Format

The system returns:

Top 3 predicted tags
Confidence score for each tag

Example:

[('Login Issue', 0.88), ('Account Access', 0.82), ('Technical Support', 0.60)]
 Zero-Shot vs Few-Shot (Concept)
Method	Description
Zero-shot	No training, uses labels only
Few-shot	Uses examples in prompt
Fine-tuned	Model trained on dataset

 This project implements Zero-shot classification.

🛠️ Technologies Used
Python 
HuggingFace Transformers 
PyTorch 
 Skills Gained
LLM-based text classification
Zero-shot learning
Multi-class prediction
NLP fundamentals
 Future Improvements
Add Few-shot prompting
Build Streamlit Web App
Improve label set
Add dataset-based evaluation
 Author

Ali
