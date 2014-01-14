var XMLWriter = require('xml-writer');

xw = new XMLWriter;
xw.startElement('version');
xw.startElement('sce_version').text('test_sce').endElement();
xw.startElement('osee_version').text('test_osee').endElement();

xw.endElement();

console.log(xw.toString())

