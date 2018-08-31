var publicidad = new Array();
publicidad[0] = "<a href='//affiliates.mozilla.org/link/banner/53165' target='_blank'><img src='//affiliates.mozilla.org/media/uploads/banners/13a610e3d140ae0b9ea7ad2a7c0f77ddba007c4b.png' class='img-responsive img-center'></a>";
publicidad[1] = "<a href='http://turpial.org.ve/' target='_blank'><img src='http://www.ubuntu.org.ve/sites/all/themes/udtheme/images/turpial.png' class='img-responsive img-center'></a>";
publicidad[2] = "<a href='http://valenciadelrey.com.ve/' target='_blank'><img src='http://valenciadelrey.com.ve/banner/loveval2.jpg' class='img-responsive img-center'></a>";
publicidad[3] = "<a href='//affiliates.mozilla.org/link/banner/42597' target='_blank'><img src='//affiliates.mozilla.org/media/uploads/banners/75e624f195107db70dc78c7c496cd76fde65af73.png' class='img-responsive img-center'></a>";
publicidad[4] = "<a href='http://www.avisosdigitales.net' target='_blank'><img src='http://www.avisosdigitales.net/web/images/logo-tw2i.png' class='img-responsive img-center'></a>";
publicidad[5] = "<a href='https://www.digitalocean.com/?refcode=1704b8c185f5 ' target='_blank'><img src='http://static.abr4xas.org/DO_Logo_Vertical_Blue-75e0d68b.png' class='img-responsive img-center'></a>";


//publicidad[N] = "<a href='url' target='_blank'><img src='url/img'></a>";
// hacemos el random
var banner = publicidad[Math.floor(Math.random() * publicidad.length)];
