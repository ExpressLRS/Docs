function getBytesFromWordArray(wordArray) {
  const result = [];

  result.push(wordArray.words[0] >>> 24);
  result.push((wordArray.words[0] >>> 16) & 0xff);
  result.push((wordArray.words[0] >>> 8) & 0xff);
  result.push(wordArray.words[0] & 0xff);

  result.push(wordArray.words[1] >>> 24);
  result.push((wordArray.words[1] >>> 16) & 0xff);

  return result;
}

function uidBytesFromText(text) {
  const bindingPhraseFull = `-DMY_BINDING_PHRASE="${text}"`;
  const bindingPhraseFullEncoded = CryptoJS.enc.Utf8.parse(bindingPhraseFull);

  const bindingPhraseHashed = CryptoJS.MD5(bindingPhraseFullEncoded);
  const uidBytes = getBytesFromWordArray(bindingPhraseHashed);

  return uidBytes;
}

function initBindingPhraseGen() {
  const codeTags = document.getElementsByTagName("code");
  const codeTagsArr = [...codeTags];

  const emptyCodeTags = codeTagsArr.filter((codeTag) => {
    return codeTag.innerText.trim() === "";
  });

  if (emptyCodeTags.length !== 2) {
    return;
  }

  const [output, bfOutput] = emptyCodeTags;

  function setOutput(text) {
    const uidBytes = uidBytesFromText(text);

    output.textContent = uidBytes;
    bfOutput.textContent = `set expresslrs_uid = ${uidBytes}\nsave`;
  }

  function updateValue(e) {
    setOutput(e.target.value);
  }

  const input = document.querySelector(".bp-input");

  if (!input) {
    return;
  }

  input.addEventListener("input", updateValue);
  setOutput("");
}
