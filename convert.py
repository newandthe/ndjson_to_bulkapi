import json

input_file = "crawl_yhn.json"  # 입력 파일 이름
output_file = "output.json"  # 출력 파일 이름

with open(input_file, "r", encoding="utf-8-sig") as f_in, open(output_file, "w", encoding="utf-8-sig") as f_out:
    data = json.load(f_in)
    for item in data:
        try:
            doc_id = item["_id"]
            doc_data = {
                "writer": item["writer"],
                "write_date": item["write_date"],
                "category_one_depth": item["category_one_depth"],
                "category_two_depth": item["category_two_depth"],
                "title": item["title"],
                "url": item["url"],
                "thumbnail_url": item["thumbnail_url"],
                "contents": item["contents"],
            }

            output_data = {
                "index": {
                    "_index": "estest",
                    "_id": doc_id
                }
            }

            f_out.write(json.dumps(output_data, ensure_ascii=False) + "\n")
            f_out.write(json.dumps(doc_data, ensure_ascii=False) + "\n")
        except KeyError as e:
            print(f"KeyError: {str(e)}")
