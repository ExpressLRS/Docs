// This code helps in linking Table of content with Admonition title

var elements = document.getElementsByClassName('custom-heading');
  
for (var i = 0; i < elements.length; i++) {
    var ele = elements[i];
    // data-id should be distinct,unique, increment by 1 and starts from 1
    var id = ele.getAttribute('data-id');
    var ele_parent_id = ele.parentElement.id;
    var count_detail = document.getElementsByTagName('details').length

    if (id != undefined && id >= 1 && id <= count_detail) {
        var ele_detail = document.getElementsByTagName('details')[id - 1];
        var content = ele_detail.children[0].innerHTML;
        ele_detail.children[0].innerHTML = content + ' <a class="headerlink" href="#' + ele_parent_id + '" title="Permanent link">¶</a>';
        ele_detail.id = ele_parent_id;
    }
}

// Removing all custom headings
while (elements.length) {
    elements[0].parentElement.remove();
}