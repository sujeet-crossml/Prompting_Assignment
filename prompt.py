# few shot prompting
fewshot_prompt ='''
sentiment = 'This movie is very bad'

Give me some sentimetal analysis for sentiment
take few examples:
        1. 'i hate comedy' : Negative
        2. 'i love this comedy show' : Positive
        3. ' this movie is okay' : Neutral

give me output in <sentiment>: <result>
replace <sentiment> to original text and <result> to analysis result
'''
# Role base prompting
role_prompt= '''
Role: Act as a 10 years of experienced movie analyst. You have done  over 10,00,000 of sentiments analyst.

Now According to your experience and number of analysis done, give me sentimental analysis of above:
            sentiment = 'This movie is have good concept of story. 
            But not the applied the better line of story for love and dialogues as other movies'
            take few examples:
                    1. 'i hate comedy' : Negative
                    2. 'i love this comedy show' : Positive
                    3. ' this movie is okay' : Neutral

            give me output in <sentiment>: <result>
            replace <sentiment> to original text and <result> to analysis result

'''

# System Prompt
system_instruction = '''
You are a senior movie sentiment analysis engine with 10+ years of
professional film criticism experience and over 10,00,000 annotated
movie reviews used for training and evaluation.
'''
# Chain of thoughts Prompting
cot_prompt = '''
You are a senior movie sentiment analyst with 10+ years of experience and over 10,00,000 movie reviews analyzed.

Follow these steps STRICTLY before giving the final answer:

Step 1: Identify key emotional signals in the review. If not able to identify emotions signal take it as nuetral and then go for next step.
(positivity, negativity, disappointment, excitement, etc.).

Step 2: Categorize each emotion as:
- Positive
- Negative
- Neutral

Step 3: Evaluate the overall emotional balance. Give more importance to story, pacing, and viewer satisfaction
If these aspect is not enough for evaluation than go to technical aspects like visuals or music.

Step 4: Decide the final sentiment label using only one of:
Positive, Negative, Mixed

Output Format (follow exactly):
<sentiment>: <result>
<1-2 sentence justification>

Movie Review:
"The movie had stunning visuals and a powerful soundtrack, but the story felt predictable and the pacing was painfully slow.
By the end, I felt disappointed despite the strong performances."
'''

# Tree of thought Prompt
tot_prompt = '''
You MUST follow the steps in order and evaluate each and every reasoning branch independently before combining them.

STEP 1: Aspect-Level Thought Branching. Independently analyze the sentiment expressed for each aspect below. Treat each aspect as a separate reasoning branch:

- Acting
- Story / Screenplay
- Pacing / Narrative Flow
- Visuals and Emotional Impact

STEP 2: Aspect Sentiment Assignment. For each aspect, assign exactly one sentiment label:
- Positive
- Negative
- Neutral

Base the label ONLY on explicit statements in the review. Do NOT infer unstated opinions.

STEP 3: Thought Aggregation (Root Decision)

Combine the aspect-level sentiments using the following rules:
1. Explicit frustration, confusion, or discouragement strongly impacts final sentiment.
2. If both positive and negative sentiments are present without a clear dominance, choose Mixed.
3. Choose ONLY ONE final sentiment label:
   Positive, Negative, or Mixed.

Output format (STRICT):

Acting: <Positive | Negative | Neutral>
Story: <Positive | Negative | Neutral>
Pacing: <Positive | Negative | Neutral>
Visuals & Emotions: <Positive | Negative | Neutral>

Overall Sentiment: <Positive | Negative | Mixed>

Review:
"This cop movie about drugs is badly told. Bad screenplay.
The premonition thing isn't properly integrated. It's confusing.
Too bad the production and cast are good. Don't bother."
'''

# contextual prompting
contextual_prompt = '''
You operate inside a large-scale streaming platform where sentiment classification directly affects recommendations, marketing decisions,
and content investment.

Domain Context (MOVIE ANALYSIS):
- Narrative quality (story, pacing, climax, ending) has the highest influence on viewer satisfaction.
- Technical elements (visuals, soundtrack, performances) are secondary.
- Explicit expressions of disappointment, regret, or dissatisfaction outweigh moderate praise.
- The final emotional state of the reviewer strongly biases sentiment.

Sentiment Ontology (STRICT):
You must choose exactly one label from:
- Positive
- Negative
- Mixed

Definitions:
- Positive → Predominantly positive emotional tone with satisfaction.
- Negative → Predominantly negative emotional tone or dissatisfaction.
- Mixed → Clear presence of both positive and negative emotions with no dominant polarity.

Analysis Constraints:
1. Analyze only the content explicitly stated in the review.
2. Do not infer unstated opinions or exaggerate emotions.
3. Detect emotional tone before assigning sentiment.
4. If both praise and criticism exist, evaluate their relative impact using the domain context above.
5. If sentiment remains ambiguous, default to Mixed.
6. Do not reveal internal reasoning steps.
7. Maintain neutral, professional language.

OUTPUT FORMAT (MANDATORY):
<sentiment>: <result>
<1-2 sentence justification>


Movie Review:
"The movie had stunning visuals and a powerful soundtrack, but the story
felt predictable and the pacing was painfully slow. By the end, I felt
disappointed despite the strong performances."

'''


# self consistency Prompt
consistency_prompt = '''
Your task is to determine the sentiment of the given movie review.

Instructions (IMPORTANT):

1. Independently analyze the review MULTIPLE times (at least 3).
   Each analysis must be done as if it is a fresh evaluation.

2. For EACH independent analysis, provide:
   a. Brief reasoning (1-2 sentences)
   b. How you evaluated the sentiment (what aspects mattered most)
   c. A final sentiment label chosen ONLY from:
      Positive, Negative, Mixed

3. Do NOT reuse wording or reasoning between analyses.
4. Base all decisions strictly on the review text.
5. Do NOT introduce new assumptions or external context.

Final Aggregation Step:

After completing all independent analyses:
- Compare the final sentiment labels.
- Select the sentiment that appears MOST FREQUENTLY.
- If there is no clear majority, default to Mixed.

Final Output Format (STRICT):

Analysis 1:
Brief reasoning:
Evaluation method:
Final sentiment:

Analysis 2:
Brief reasoning:
Evaluation method:
Final sentiment:

Analysis 3:
Brief reasoning:
Evaluation method:
Final sentiment:

Self-Consistent Final Answer:
Final sentiment:
Reason for selection (1 sentence):

REVIEW TO ANALYZE:
“The acting was powerful and emotionally convincing, but the screenplay was weak and the ending felt rushed.”
'''
