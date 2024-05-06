from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


def get_translation(text):

    model_name = "unicamp-dl/translation-en-pt-t5"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    enpt_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)
    
    return enpt_pipeline(f"translate English to Portuguese: {text}")