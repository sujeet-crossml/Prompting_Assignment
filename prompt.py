# few shot prompting
prompt1 ='''
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
prompt2= '''
Role: Act as a 10 years of experienced movie analyst. You have done  over 10,00,000 of sentiments analyst.

Now According to your experience and number of analysis done, give me sentimental analysis of above:
            sentiment = 'This movie is have good concept of story. But not the applied the better line of story for love and dialogues as other movies'
            take few examples:
                    1. 'i hate comedy' : Negative
                    2. 'i love this comedy show' : Positive
                    3. ' this movie is okay' : Neutral

            give me output in <sentiment>: <result>
            replace <sentiment> to original text and <result> to analysis result

'''

# System Prompt
system_instruction = '''
"Act as a 10 years of experienced movie analyst and your name is G-5. You have done  over 10,00,000 of sentiments analyst."
'''
# Chain of thoughts Prompting
prompt3 = '''
You are a senior movie sentiment analyst with 10+ years of experience
and over 1,000,000 movie reviews analyzed.

Follow these steps STRICTLY before giving the final answer:

Step 1: Identify key emotional signals in the review
(positivity, negativity, disappointment, excitement, etc.).

Step 2: Categorize each emotion as:
- Positive
- Negative
- Neutral

Step 3: Evaluate the overall emotional balance.
Give more importance to story, pacing, and viewer satisfaction
than to technical aspects like visuals or music.

Step 4: Decide the final sentiment label using ONLY one of:
Positive, Negative, Mixed

Output Format (follow exactly):
<sentiment>: <result>
<1-2 sentence justification>

Movie Review:
"The movie had stunning visuals and a powerful soundtrack, but the story felt predictable and the pacing was painfully slow.
By the end, I felt disappointed despite the strong performances."
'''

# self consistency Prompt
prompt4 = '''

determine sentiment analysis of the given reviews and provide.
1. Brief reasoning
2. how you evalute for this answer.
3. Final sentiment (Positive, Negative, or Mixed)

Review:
        “The acting was powerful and emotionally convincing, but the screenplay was weak and the ending felt rushed.”
'''

# Tree of thought Prompt
prompt5 = '''
Use following rules given below and analyse the sentimen analysis:
rule 1: Identify sentiment for each:
- Acting
- Story
- Pacing
- Visuals and emotions

rule 2: give the sentiment (positive, negative, neutral) to each.

Step 3: Combine the all sentiments and decide the overall sentiment
(Positive, Negative, or Mixed).

Review:
        "This cop movie about drugs is badly told. Bad screen play. The premonition thing isn't properly integrated.
          It's confusing. Too bad the production and cast are good. Don't bother."
'''
