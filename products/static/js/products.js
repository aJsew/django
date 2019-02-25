const renderProduct = ({id, name, description,  cost}) => (
    '
        <div class="productss">
            <div class="propuct_item">
                <span class="propuct_item-name">
                    ${ name }
                </span>
                <span class="propuct_item-description">
                    ${ description }
                </span>
                <span>
                    ${ cost ? cost : 'Значение отсутствует'}
                </span>
                <a href="/products/${ id }" class="">CCblJlKA HA ${ name }</a>
            </div>
        </div>
    '
)