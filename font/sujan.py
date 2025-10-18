import os
import json

# বর্তমান ফোল্ডার (যেখান থেকে স্ক্রিপ্ট চালানো হবে)
current_folder = os.getcwd()

# সব ফাইলের নাম নেওয়া (ফোল্ডার বাদ দিয়ে)
file_names = [f for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f))]

# JSON ডাটা তৈরি
data = {"files": file_names}

# JSON ফাইল সংরক্ষণ
output_file = os.path.join(current_folder, "file_list.json")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


print(f"✅ File list saved successfully as: {output_file}")
