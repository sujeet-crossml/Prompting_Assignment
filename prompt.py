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
# Chain of thoughts Prompting
prompt3 = '''
Act as a 10 years of experienced movie analyst. You have done  over 10,00,000 of sentiments analyst.

Your task is to analyse the movies review sentiments with the following rule considering:
    1. Look at the tones and emotions of reviews.
    2. Analyse whether the emotion is positive, negative, neutral/mixed.
    3. After that decide the sentiment label.

give me output in this format:
         <sentiment>: <result>
         Little bit justification( 1  or 2 sentences)

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