import streamlit as st

with st.sidebar:
    st.subheader("About")
    st.markdown('This app intended to correct text output created when UTF-8 is interpreted as Win1252 or ISO 8859-1. This should correct characters in a string to the expected Unicode.')
    st.markdown('If you are unsure what I mean by this, please refer to the "Expected" and "Actual" character columns <a href="https://www.i18nqa.com/debug/utf8-debug.html">at this helpful website</a>.', unsafe_allow_html=True)
    st.subheader("Contact")
    st.markdown('This is a work-in-progress. If you discover any issues, you\'re welcome to reach out to me <a href="mailto:the@andrewharris.dev">via email</a>.', unsafe_allow_html=True)
    
st.title('UTF-8 Encoding Debugger')
st.caption('For further explanation, please check the left sidebar.')
with st.container():
    input_sentence = st.text_area("Please input text here.")
    submit = st.button('Debug String/Text')

input_text = input_sentence
dictionary = {
"`": "'",
'â‚¬': '€',
'â€š': '‚',
'Æ’': 'ƒ',
'â€ž': '„',
'â€¦': '…',
'â€ ': '†',
'â€¡': '‡',
'Ë†': 'ˆ',
'â€°': '‰',
'â€¹': '‹',
'Å’': 'Œ',
'Å½': 'Ž',
'â€˜': '‘',
'â€™': '’',
'â€œ': '“',
'â€¢': '•',
'â€“': '–',
'â€”': '—',
'Ëœ': '˜',
'â„¢': '™',
'Å¡': 'š',
'â€º': '›',
'Å“': 'œ',
'Å¾': 'ž',
'Å¸': 'Ÿ',
'Â¡': '¡',
'Â¢': '¢',
'Â£': '£',
'Â¤': '¤',
'Â¥': '¥',
'Â¦': '¦',
'Â§': '§',
'Â¨': '¨',
'Â©': '©',
'Âª': 'ª',
'Â«': '«',
'Â¬': '¬',
'Â­': '-',
'Â®': '®',
'Â¯': '¯',
'Â°': '°',
'Â±': '±',
'Â²': '²',
'Â³': '³',
'Â´': '´',
'Âµ': 'µ',
'Â¶': '¶',
'Â·': '·',
'Â¸': '¸',
'Â¹': '¹',
'Âº': 'º',
'Â»': '»',
'Â¼': '¼',
'Â½': '½',
'Â¾': '¾',
'Â¿': '¿',
'Ã€': 'À',
'Ãƒ': 'Ã',
'Ã„': 'Ä',
'Ã…': 'Å',
'Ã†': 'Æ',
'Ã‡': 'Ç',
'Ãˆ': 'È',
'Ã‰': 'É',
'ÃŠ': 'Ê',
'Ã‹': 'Ë',
'ÃŒ': 'Ì',
'ÃŽ': 'Î',
'Ã‘': 'Ñ',
'Ã’': 'Ò',
'Ã“': 'Ó',
'Ã”': 'Ô',
'Ã•': 'Õ',
'Ã–': 'Ö',
'Ã—': '×',
'Ã˜': 'Ø',
'Ã™': 'Ù',
'Ãš': 'Ú',
'Ã›': 'Û',
'Ãœ': 'Ü',
'Ãž': 'Þ',
'ÃŸ': 'ß',
'Ã¡': 'á',
'Ã¢': 'â',
'Ã£': 'ã',
'Ã¤': 'ä',
'Ã¥': 'å',
'Ã¦': 'æ',
'Ã§': 'ç',
'Ã¨': 'è',
'Ã©': 'é',
'Ãª': 'ê',
'Ã«': 'ë',
'Ã¬': 'ì',
'Ã­': 'í',
'Ã®': 'î',
'Ã¯': 'ï',
'Ã°': 'ð',
'Ã±': 'ñ',
'Ã²': 'ò',
'Ã³': 'ó',
'Ã´': 'ô',
'Ãµ': 'õ',
'Ã¶': 'ö',
'Ã·': '÷',
'Ã¸': 'ø',
'Ã¹': 'ù',
'Ãº': 'ú',
'Ã»': 'û',
'Ã¼': 'ü',
'Ã½': 'ý',
'Ã¾': 'þ',
'â€': '”',
'Å': 'Š',
'Ã‚': 'Â',
'Ã': 'à',
'Â­': '­',
'Ã¿': 'ÿ'}

for item in dictionary:
    if item in input_text:
        input_text = input_text.replace(item,dictionary[item])


with st.container():
    st.subheader("Output")
    st.write(input_text)
