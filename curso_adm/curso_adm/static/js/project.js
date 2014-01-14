var id_navbar;
var URL = document.URL;

// não alterar ordem da empresa e categoriaempresa
var ids = ['signup', 'cargo', 'empresa', 'categoriaempresa', 'perfil', 'signin', 'user'];

var idslen = ids.length;
for ( var i = idslen ; i-- ; ) {
    var id = ids[i];
    if( URL.indexOf(id) != -1 ){
        id_navbar = id;
        break;
    }
    id_navbar = 'home';
}
$( '#id_' + id_navbar + '_navbar' ).addClass( 'active' );
