var demo4 = new CircleType(document.getElementById("inst")).radius(500);

function img_1() {
  window.scrollTo(0, 0);
  domtoimage
    .toPng(document.getElementById("cont_1"))
    .then(function (dataUrl) {
      var img = new Image();
      img.src = dataUrl;
      document.body.appendChild(img);
      let imagePath = img.getAttribute("src");
      let fileName = "cover.png";
      saveAs(imagePath, fileName);
      document.body.removeChild(img);
    })
    .catch(function (error) {
      console.error("oops, something went wrong!", error);
    });
}

function img_2() {
  window.scrollTo(0, 0);
  domtoimage
    .toPng(document.getElementById("cont_2"))
    .then(function (dataUrl) {
      var img = document.createElement("img");
      img.src = dataUrl;
      img.id = "dummy_2_img";
      document.body.appendChild(img);
      let imagePath = img.getAttribute("src");
      let fileName = "cover.png";
      saveAs(imagePath, fileName);
      document.body.removeChild(img);
    })
    .catch(function (error) {
      console.error("oops, something went wrong!", error);
    });
}
