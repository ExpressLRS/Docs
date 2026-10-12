// This code helps in linking Table of content with Admonition title

// Zensical copies heading markup into the sidebar TOC, so match only the
// headings in the page body or the TOC entries get removed along with them
var elements = document.querySelectorAll(':is(h1, h2, h3, h4, h5, h6) > .custom-heading');
  
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
for (var i = 0; i < elements.length; i++) {
    elements[i].parentElement.remove();
}