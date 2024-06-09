import os
import json


def links_parser(
    txt_file: str = "links_data.txt",
    save_as_json: bool = False,
    saved_file: str = "parsed_links_data",
) -> dict:
    """
    Extract and parse notes from text file (manually (!) created from original apple notes app)

    :param txt_file: notes in plain text file copied manually from apple notes
    :param save_as_json: if to save to json or just parse
    :param saved_file: file name to be saved to (JSON)
    :return: dict object with topics as keys and corresponding values as list of links
    """

    with open(txt_file) as f:
        data = f.readlines()
        data = data[1:]
        data = [i.strip() for i in data if i != "\n"]
        data = [
            i if ("https" not in i) or ("http" not in i) else i.strip("*").strip()
            for i in data
        ]

        # for removing utm query parameter - case 1 (first query param)
        data = [i.split("?utm_")[0] if "?utm_" in i else i for i in data]

        # for removing utm query parameter - case 2 (not the first query param)
        data = [i.split("&utm_")[0] if "&utm_" in i else i for i in data]

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
        with open(f"{os.getcwd()}/{saved_file}.json", "w") as f:
            json.dump(parsed_data, f)

    for k, v in parsed_data.items():
        print(f"{k} - {len(v)}")

    return parsed_data


if __name__ == "__main__":
    # pprint(main(save_as_json=False), indent=4)
    links_parser(save_as_json=True)
