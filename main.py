import json
def evaluate_model(gold, predictions):
    """
    Comparing gold and AI's response for  prompts
    """
    total = 0
    correct = 0
    errors = []
    for chat_id in gold:
        for field in gold[chat_id]:
            total += 1
            gold_value = gold[chat_id][field]
            pred_value = predictions.get(chat_id, {}).get(field)
            if gold_value == pred_value:
                correct += 1
            else:
                errors.append({
                    "chat_id": chat_id,
                    "field": field,
                    "gold": gold_value,
                    "predicted": pred_value
                })
    return {
        "total_fields": total,
        "correct": correct,
        "missed": total - correct,
        "accuracy": round(correct / total, 3),
        "errors": errors
    }
def main():
    with open("/Users/leelasaigottimukkala/Desktop/Commverse/Golddata.json", "r") as f:
        gold = json.load(f)
    with open("/Users/leelasaigottimukkala/Desktop/Commverse/Deepseek_prompt5.json", "r") as f:
        gpt5_v1 = json.load(f)
    results = evaluate_model(gold, gpt5_v1)
    print("DEEPSEEK + prompt v5 evaluation")
    print("***************************************")
    print("Total fields:", results["total_fields"])
    print("Correct:", results["correct"])
    print("Missed:", results["missed"])
    print("Accuracy:", results["accuracy"])
    print("\nSample Errors (first 10):")
    for err in results["errors"][:10]:
        print(err)


if __name__ == "__main__":
    main()
