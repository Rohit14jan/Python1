# "Transformers" created by vasvani et.al (2017) "Attention is all you need"

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


def LoadTokenizerModel(modelName="microsoft/DialoGPT-medium"):
    print("loading model")
    tokenizer = AutoTokenizer.from_pretrained(modelName)
    model = AutoModelForCausalLM.from_pretrained(modelName)
    print("finish loading model")
    return tokenizer,model

tokenizer,model = LoadTokenizerModel(modelName="microsoft/DialoGPT-medium")

def readInput(tokenizer):
    myInput = input("You: ")
    inputIDS = tokenizer.encode(myInput + tokenizer.eos_token, return_tensors='pt')

    return inputIDS

def generateResponse(tokenizer,model):
    inputIDs = readInput(tokenizer)
    chatOutput = model.generate(inputIDs,max_length = 1250, pad_token_id = tokenizer.eos_token_id)
    chatOutputText = tokenizer.decode(chatOutput[:,inputIDs.shape[-1]:][0], skip_special_tokens= True)
    print("Model >", chatOutputText)

generateResponse(tokenizer,model)


def generateResponseForRoundn(tokenizer,model,chatRound,chatHistory):
    inputIDs = readInput(tokenizer)

    allInputs = None
    if chatRound==0:
        allInputs = inputIDs
    else:
        allInputs = torch.cat([chatHistory,inputIDs],dim=-1)


    allChatOutputsSoFar = model.generate(allInputs,max_length = 1250, pad_token_id = tokenizer.eos_token_id)
    chatOutputText = tokenizer.decode(allChatOutputsSoFar[:,allInputs.shape[-1]:][0], skip_special_tokens= True)
    print("Model >", chatOutputText)
    return allChatOutputsSoFar
def chatForNRounds(n=20):
    tokenizer,model = LoadTokenizerModel(modelName="microsoft/DialoGPT-medium")
    chatHistory = None
    for chatRound in range(n):
        chatHistory = generateResponseForRoundn(tokenizer,model,chatRound,chatHistory)

chatForNRounds(n=20)
