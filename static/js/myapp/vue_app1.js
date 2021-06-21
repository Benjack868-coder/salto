Vue.component('show-members-dialog', {
    methods: {
        'getMembers':function(event){
            var self = this
            var members = {}
            $.ajax({
                type : 'GET',
                url : 'http://localhost:8000/member/all/',
                data : {
                    'action':'ALL',
                    'tournament_id': $('input[name="tournament_id"]').val()
                },
                success: function(data){

                },
                error: function(e){
                    alert(JSON.stringify(e))
                }
            }).done(function(data){
                self.members = data
            })
        },
        'selectMember': function(event, member_id){
            $('.owner-list').removeClass('active')
            $('#'+member_id).addClass('active')
            this.member_id = member_id
        },
        'getOwner': function(event, member_id){
            if(member_id !=0){
                $.ajax({
                    type : 'GET',
                    url : 'http://localhost:8000/member/all/',
                    data : {
                        'action':'GET_MEMBER_INFO',
                        'member_id': member_id
                    },
                    success: function(data){

                    },
                    error: function(e){
                        alert(JSON.stringify(e))
                    }
                }).done(function(data){
                    $('input[name="member_id"]').val(data[0].id)
                    $('input[name="owner"]').val(data[0].owner)
                    $('input[name="email"]').val(data[0].email)
                    $('input[name="entry_name"]').val(data[0].owner +' Gaming')
                    $('input[name="contact_number"]').val(data[0].contact_number)
                    $('#exampleModalScrollable').modal('hide')
                })
            }
        },
        'searchOwner': function(event){
            var self = this
            self.keywords = event.target.value
            $.ajax({
                type : 'GET',
                url : 'http://localhost:8000/member/all/',
                data : {
                    'action':'SEARCH',
                    'tournament_id': $('input[name="tournament_id"]').val(),
                    'keywords': self.keywords
                },
                success: function(data){

                },
                error: function(e){
                    alert(JSON.stringify(e))
                }
            }).done(function(data){
                self.members = data
            })

        },
    },
    data: function(){
        return {
            members : {},
            member_id : 0,
            keywords : {},
        }
    },
    template:
    `
        <div class="float-right">
            <!-- Button modal trigger -->
            <button @click="getMembers()" class="btn btn-primary btn-sm" type="button" data-toggle="modal" data-target="#exampleModalScrollable"><i class="fas fa-users fa-xs"></i> Members</button>

            <!-- Modal -->
            <div class="modal fade" id="exampleModalScrollable" tabindex="-1" role="dialog" aria-labelledby="exampleModalScrollableTitle" aria-hidden="true">
                <div class="modal-dialog modal-dialog-scrollable modal-xs" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalScrollableTitle">Modal title</h5>
                            <button class="close" type="button" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                        </div>
                        <div class="modal-body">
                            <div class="row">
                                <div class="col-lg-12">
                                    <input @keyup.enter="searchOwner($event, )" type="text" class="form-control rounded-0" placeholder="Search owner...."/>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <ul class="list-group rounded-0" style="margin-top:10px">
                                        <li v-if="!members.length" class="list-group-item d-flex justify-content-between align-items-center list-group-item-warning">
                                            No result found
                                        </li>
                                        <li v-for="member in members" @click="selectMember($event, member.id)" v-bind:id="member.id" class="list-group-item d-flex justify-content-between align-items-center owner-list">
                                            {{member.owner}}
                                            <span v-if="member.count != 0" class="badge badge-primary badge-pill">{{member.count}}</span>
                                        </li>
                                    </li>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer"><button class="btn btn-secondary" type="button" data-dismiss="modal">Close</button><button @click="getOwner($event, member_id)" class="btn btn-primary" type="button">SELECT</button></div>
                    </div>
                </div>
            </div>
        </div>
    `
})

var salto = new Vue({
    el: '#wrapper',
    delimiters: ["[[","]]"],

    data : {
        message : 'Hai from Vue Js',
    }

})
