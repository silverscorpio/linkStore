// for list views (table)
DataTable.datetime('d MMM yy');
let table = new DataTable('#listTable', {
    lengthMenu: [10, 25, 50, {label: 'All', value: -1}],
    layout: {
        topStart: 'pageLength',
        topEnd: {
            search: {
                placeholder: 'Search LinkStore',
            }
        },
        bottomStart: 'info',
        bottomEnd: 'paging'
    }
})