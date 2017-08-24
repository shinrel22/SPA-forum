<template>
  <div :id="identify.id">
    <div class="row">
      <div class="col-xs-9">
        <table class="table table-responsive m-0 card-box forum-main-table">
          <thead>
          <tr>
            <th style="width: 50%">Đại Sảnh</th>
            <th style="text-align: center">Threads</th>
            <th style="text-align: center">Posts</th>
            <th>Last Post</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td>
              <div class="row-title">
                <div class="row-icon">
                  <span class="fa fa-comment"></span>
                </div>
                <div>
                  <span class="row-header">1231</span>
                  <div>Some thing here</div>
                </div>
              </div>
            </td>
            <td style="text-align: center">1</td>
            <td style="text-align: center">1</td>
            <td>1241231231241231231231</td>
          </tr>
          </tbody>
        </table>
      </div>
      <div class="col-xs-3">
        <div class="panel panel-color panel-inverse">
          <div class="panel-heading">
            <h3 class="panel-title">Recent Posts</h3>
          </div>
          <div class="panel-body">
            <div class="comment-text m-b-10">
              <div class="comment-header">
                <a href="#" title="">Re: what the fuck aaaaaaas asd asda das dasd asdas dasd asd?</a>
              </div>
              <span class="text-muted">By no one</span>
              <div class="m-t-5">Fuck that bitch 1231231231123123 1231 23123123 123 123 12312 312 323123</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    props: {
      identify: {type: Object, default () { return {id: 'home', name: 'Home'} }}
    },
    data () {
      return {
        COLUMNS: [
          {
            title: 'Topics',
            style: {
              'text-align': 'center'
            }
          },
          {
            title: 'Views',
            'text-align': 'center'
          },
          {
            title: 'Last Post'
          }
        ]
      }
    }
  }
</script>
<style scoped=""></style>
