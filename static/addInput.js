var counterText = 2;
var counterRadioButton = 0;
var counterCheckBox = 0;
var counterTextArea = 0;
function addInputs(divName, inputType, placeholderName){
	var newdiv = document.createElement('div');
	switch(inputType) {
		case 'text':
			//newdiv.innerHTML = "<input type='text' name='"+ divName + "[" + counterText + "]'>";
			newdiv.innerHTML = "<input type='text' placeholder='"+placeholderName+"' id='new-skill' name='"+ divName + "'>";
			counterText++;
			break;
		case 'radio':
			newdiv.innerHTML = "Entry " + (counterRadioButton + 1) + " <br><input type='radio' name='myRadioButtons[]'>";
			counterRadioButton++;
			break;
		case 'checkbox':
			newdiv.innerHTML = "Entry " + (counterCheckBox + 1) + " <br><input type='checkbox' name='myCheckBoxes[]'>";
			counterCheckBox++;
			break;
		case 'textarea':
			newdiv.innerHTML = "Entry " + (counterTextArea + 1) + " <br><textarea name='myTextAreas[]'>type here...</textarea>";
			counterTextArea++;
			break;
	}
	document.getElementById(divName).appendChild(newdiv);
}
