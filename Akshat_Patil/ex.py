from transformers import BartForConditionalGeneration, BartTokenizer
from rouge_score import rouge_scorer

# Load the saved model
model_path = "C:/Users/91862/Desktop/Text_Sum_Infosys/saved_model"
model = BartForConditionalGeneration.from_pretrained(model_path)
tokenizer = BartTokenizer.from_pretrained(model_path)

# Input text
input_text = """
Arsene Wenger admits he is concerned Theo Walcott’s confidence is plummeting after his struggles with England this week. The Arsenal manager will have a heart-to-heart chat with the forward ahead of Saturday’s crunch top-four clash against Liverpool. Walcott was hauled off after 55 minutes of England’s 1-1 draw in Italy on Tuesday night. Theo Walcott struggled for England and Arsene Wenger admits he is concerned by the winger's confidence . Walcott was replaced by Ross Barkley after just 55 minutes of England's 1-1 draw against Italy . 2 - Premier League goals for Walcott this season - his average haul per season during his time at Arsenal is 5.6. It was the latest disappointment in a difficult season for the 26-year-old, who has struggled for game time since returning from a long-term lay-off due to a serious knee injury. With Alex Oxlade-Chamberlain out of Liverpool’s visit due to a hamstring strain, and Danny Welbeck a major doubt after sustaining a knee problem on international duty, Walcott could start on Saturday. But Wenger said: ‘Yes, I’m worried about Theo’s confidence. He’s sensitive and I’m a bit concerned about the damage that game can have on his mind. Walcott could face Liverpool on Saturday with Alex Oxlade-Chamberlain injured and Danny Welbeck a doubt . ‘He’s not completely there yet (after the injury). But being exposed like that, people have a harsh judgement on him that is not deserved because he does well. ‘At the moment he is frustrated, but that is normal. I will speak with him, but I think he is strong enough. ‘I will see what state of mind he is in. We always have a word, if it is a positive experience or a negative experience, you ask “how did it go?”. We always speak about the last game. ‘He is not fragile mentally, he is strong mentally but he is disappointed because when you come back from an injury you always think you are ready. ‘He needs patience. He is at the moment not in his best mood. ‘He has big confidence in himself and he has gone through some difficult periods in his life and he has always come out with strength.’ Arsenal boss Wenger says he will speak with Walcott but believes the Gunners winger is 'strong enough' Walcott found himself playing in the No 10 role for England in Turin — a role he is not accustomed to. And Wenger admitted he was surprised to see the pacy forward in such an unfamiliar position. ‘Have I ever seen him play No 10 in training or anything? No,’ said Wenger. ‘Theo’s strength is the quality of his movements, he wants to go to get on the end of things. He’s not a guy who provides. ‘I don’t think it was the intention of Roy Hodgson to play him there. It’s maybe because Wayne Rooney took the initiative during the game to play higher up and tell Theo to drop back. ‘I didn’t see Roy Hodgson in the game stand up to say “Walcott, you come and play in midfield and Rooney you go up front”. That’s an initiative they took on the pitch.’ Walcott aims a shot at goal during England's friendly against Italy at the Juventus Stadium in Turin . Walcott was starting his first international game in 18 months having injured his cruciate ligaments . Meanwhile, Wenger insists there are fundamental flaws in FA chairman Greg Dyke’s proposal to increase the number of required homegrown players in Premier League squads to 12. Dyke believes increasing the number of British players in squads will help contribute to a more successful England team. But Wenger said: ‘I believe we are in a top level competition and you earn your right through the quality of your performance rather than your place of birth. ‘Secondly, I’m happy to, and would like to contribute to the quality of the English national team, but you have two questions you can raise before that. ‘First of all between 1966 and 1996 there were no foreign players in England and it didn’t improve too much the performances of the national team. ‘Secondly, if between the ages of 16 and 21 the England youth teams win every single competition in Europe then there is something we have to do because they are not getting their chance at the top level. Wenger believes there are flaws in FA Chairman Greg Dyke’s proposal to increase the homegrown quota . ‘That is not the case, on the contrary. I think between 16 and 21 the English youth teams, until now, have not performed. So that’s the heart of the problem. ‘Let’s get better at that level, then if there is a problem integrating these players in the top teams, we have to do something about it. ‘I think today you have to be very brave to integrate young players in the top teams because the pressure is very high. I still believe when they are good enough, they play. ‘You speak about Raheem Sterling and Harry Kane. Nobody stops the quality, no matter where they are from. So let’s focus on that first.
"""
true_summary = """
Arsene Wenger will have chat with Theo Walcott ahead of Arsenal clash . Walcott was substituted after 55 minutes of England's draw with Italy . Arsenal boss is Wenger is concerned by the winger's confidence . The Gunners take on Liverpool at the Emirates Stadium on Saturday .
"""

# Tokenize input
inputs = tokenizer([input_text], max_length=1024, return_tensors="pt", truncation=True)

# Greedy Decoding
greedy_output = model.generate(inputs["input_ids"], max_length=150, num_beams=1)
greedy_summary = tokenizer.decode(greedy_output[0], skip_special_tokens=True)

# Beam Search Decoding
beam_output = model.generate(
    inputs["input_ids"], max_length=150, num_beams=5, length_penalty=2.0, early_stopping=True
)
beam_summary = tokenizer.decode(beam_output[0], skip_special_tokens=True)

# ROUGE Score Calculation
scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
greedy_rouge = scorer.score(true_summary, greedy_summary)
beam_rouge = scorer.score(true_summary, beam_summary)

# Print Results
print("Greedy Decoding Summary:\n", greedy_summary)
print("\nBeam Search Summary:\n", beam_summary)
print("\nROUGE Scores:")
print(f"Greedy Decoding ROUGE-1: {greedy_rouge['rouge1'].fmeasure:.4f}")
print(f"Greedy Decoding ROUGE-2: {greedy_rouge['rouge2'].fmeasure:.4f}")
print(f"Greedy Decoding ROUGE-L: {greedy_rouge['rougeL'].fmeasure:.4f}")

print(f"Beam Search ROUGE-1: {beam_rouge['rouge1'].fmeasure:.4f}")
print(f"Beam Search ROUGE-2: {beam_rouge['rouge2'].fmeasure:.4f}")
print(f"Beam Search ROUGE-L: {beam_rouge['rougeL'].fmeasure:.4f}")
