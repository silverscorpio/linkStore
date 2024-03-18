# script to parse existing note of links for storing in DB
import os
import json


def main(save_as_json: bool = False) -> dict:
    with open("links.txt") as f:
        data = f.readlines()
        data = data[1:]
        data = [i.strip() for i in data if i != "\n"]
        data = [
            i if ("https" not in i) or ("http" not in i) else i.strip("*").strip()
            for i in data
        ]

    parsed_data = {}  # notes with URLs (URL notes removed)
    topics = [
        (idx, i.strip())
        for idx, i in enumerate(data)
        if (("https" not in i) or ("http" not in i))
    ]
    for v in range(len(topics)):
        if v == len(topics) - 1:
            parsed_data[topics[v][1]] = [
                j.split(" - ", maxsplit=1)[0].strip() for j in data[topics[v][0] + 1 :]
            ]
        else:
            parsed_data[topics[v][1]] = [
                j.split(" - ", maxsplit=1)[0].strip()
                for j in data[topics[v][0] + 1 : topics[(v + 1)][0]]
            ]

    if save_as_json:
        with open(f"{os.getcwd()}/parsed_data.json", "w") as f:
            json.dump(parsed_data, f)

    for k, v in parsed_data.items():
        print(f"{k} - {len(v)}")
    return parsed_data


if __name__ == "__main__":
    # pprint(main(save_as_json=False), indent=4)
    main(save_as_json=True)
