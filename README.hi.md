<div align="center">
	<img height="30" width="40" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-ico.svg">
    <a href="./README.md">
		<img height="30" width="40" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-en.svg">
	</a>
	<a href="./RREADME.ja.md">
		<img height="30" width="40" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-ja.svg">
	</a>
	<a href="./README.hi.md">
		<img height="30" width="40" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-hi.svg">
	</a>
	<a href="./README.pt-BR">
		<img height="30" width="40" src="https://github.com/hipolitorodrigues/mock_csv_generator/blob/e3f4b6240ef8b99934e7383aeafac11e1c1819d2/assets/images/img-readme-pt-br.svg">
	</a>
</div

# मॉक CSV जेनरेटर

**मॉक CSV जेनरेटर** एक डेस्कटॉप एप्लिकेशन है, जिसे Python और Tkinter का उपयोग करके विकसित किया गया है। यह उपयोगकर्ता-परिभाषित कॉन्फ़िगरेशन के आधार पर कस्टम CSV फाइलें बनाने की अनुमति देता है। परीक्षण और प्रोटोटाइपिंग के लिए मॉक डेटा उत्पन्न करने के लिए यह आदर्श है।

![alt text](https://github.com/hipolitorodrigues/mock_csv_generator/blob/88853b15db5302aba301f4e70edf7a7e2503a11f/assets/images/sampling.png)

![alt text](https://github.com/hipolitorodrigues/mock_csv_generator/blob/ad0ad82c9a6114ccceee7eed0f983b205cf64991/assets/images/screenshot.png)

## विशेषताएँ

1. **कस्टम CSV निर्माण**:
   - कस्टम हेडर और मानों के साथ कॉलम को कॉन्फ़िगर करें।
   - उत्पन्न की जाने वाली पंक्तियों की संख्या परिभाषित करें।

2. **कॉन्फ़िगरेशन प्रबंधन**:
   - **कॉन्फ़िगरेशन सहेजें**: वर्तमान कॉन्फ़िगरेशन (हेडर और कॉलम मान) को JSON फाइल में सहेजें।
   - **कॉन्फ़िगरेशन लोड करें**: पहले से सहेजे गए कॉन्फ़िगरेशन को JSON फाइल या `DATA_CONFIG.py` मॉड्यूल से लोड करें।
   - **कॉन्फ़िगरेशन साफ़ करें**: सभी कॉलम को उनकी प्रारंभिक स्थिति में रीसेट करें।

3. **उपयोगकर्ता-अनुकूल GUI**:
   - Tkinter का उपयोग करके निर्मित सहज इंटरफ़ेस।
   - 8 तक कॉन्फ़िगर करने योग्य कॉलम का समर्थन करता है।

## यह कैसे काम करता है

1. **कॉलम कॉन्फ़िगरेशन**:
   - प्रत्येक कॉलम के लिए एक हेडर जोड़ें।
   - प्रत्येक कॉलम के लिए संभावित मान जोड़ें।

2. **CSV जेनरेशन**:
   - इच्छित पंक्तियों की संख्या दर्ज करें।
   - "Generate CSV" पर क्लिक करें और `mokup-00.csv` फाइल को उसी डायरेक्टरी में बनाएं जहां प्रोग्राम है।

3. **कॉन्फ़िगरेशन प्रबंधन**:
   - अपने सेटिंग्स को सहेजने या लोड करने के लिए "Configuration" मेनू का उपयोग करें:
     - JSON फाइल से लोड करने के लिए "Load from JSON"।
     - Python मॉड्यूल से लोड करने के लिए "Load from DATA_CONFIG.py" (यदि उपलब्ध हो)।
     - वर्तमान सेटअप को सहेजने के लिए "Save Configuration"।
     - सभी कॉन्फ़िगरेशन को रीसेट करने के लिए "Clear All"।

## कैसे चलाएँ

1. **पूर्वापेक्षाएँ**:
   - Python 3.8 या उच्चतर।
   - स्टैंडर्ड लाइब्रेरी (`tkinter`, `json`, `csv`)।

2. **निष्पादन**:
   - कोड डाउनलोड करें।
   - `main.py` फाइल चलाएँ:
     ```bash
     python main.py
     ```

3. **उत्पन्न फाइलें**:
   - सहेजी गई कॉन्फ़िगरेशन `column_config.json` में संग्रहीत होंगी।
   - उत्पन्न CSV फाइल `mokup-00.csv` के रूप में सहेजी जाएगी।

## उपयोग की गई तकनीकें

- **Python 3.13.1**: लॉजिक और बैकएंड।
- **Tkinter**: सरल और उत्तरदायी ग्राफिकल इंटरफ़ेस।

## प्रोजेक्ट संरचना

- `main.py`: मुख्य एप्लिकेशन कोड।
- `column_config.json`: (वैकल्पिक) उपयोगकर्ता-सहेजे गए कॉन्फ़िगरेशन संग्रहीत करता है।
- `DATA_CONFIG.py`: (वैकल्पिक) कस्टम कॉन्फ़िगरेशन को Python मॉड्यूल के माध्यम से लोड करने की अनुमति देता है।

## लेखक

- **डेवलपर**: Hipolito Rodrigues  
- **निर्माण तिथि**: 23/01/2025  
- **अंतिम अद्यतन**: 27/01/2025  
- **वर्तमान संस्करण**: 1.3.4  

---

## लाइसेंस

यह प्रोजेक्ट [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/) लाइसेंस के तहत लाइसेंस प्राप्त है। इसका मतलब है कि आप इस कार्य को कॉपी, संशोधित, वितरित और उपयोग कर सकते हैं, यहां तक कि व्यावसायिक उद्देश्यों के लिए भी, बिना अनुमति मांगे।
