// CFI Admin SPA - Event Delegation Architecture
// Based on V8 spec: 11 tables, file upload, toast notifications

var ADMIN_TABLES = [
  {n:"site_settings",l:"网站设置",e:["value"],k:"key",nd:true},
  {n:"navigation",l:"导航管理",e:["title","title_en","url","sort_order","is_external"]},
  {n:"plans",l:"计划管理",e:["title","subtitle","description","content","slug","tags","sort_order","is_active"]},
  {n:"articles",l:"文章管理",e:["title","slug","summary","content","tags","article_type","is_published","is_featured","featured_image","featured_sort_order"]},
  {n:"reports",l:"报告管理",e:["title","slug","summary","content","tags","report_type","pdf_filename","translator","source_url","is_published","is_featured","featured_image"]},
  {n:"researchers",l:"研究员管理",e:["name","slug","title","bio","photo","tags","is_active","achievements"]},
  {n:"courses",l:"课程管理",e:["title","slug","description","instructor","qr_code","external_url","is_active"]},
  {n:"founders",l:"发起人管理",e:["name","slug","title","bio","photo","sort_order","is_active"]},
  {n:"books",l:"工具手册管理",e:["title","slug","author","summary","cover_image","buy_url","download_url","file_url","type","tags","sort_order","is_active"]},
  {n:"community_activists",l:"社群行动者管理",e:["name","slug","title","bio","photo","tags","sort_order","is_active","achievements"]},
  {n:"social_links",l:"社交媒体管理",e:["platform","url","icon","sort_order","is_active"]}
];

var S={t:"site_settings",id:null,d:null};
function Q(s){return document.querySelector(s)}
function GI(i){return document.getElementById(i)}

function api(m,p,b){var o={method:m,headers:{"Content-Type":"application/json"}};if(b)o.body=JSON.stringify(b);return fetch("/api/"+p,o).then(function(r){return r.json()})}

function loadTable(n){
  var c=GI("admin-table-container");c.innerHTML="<div class=\"admin-loading\">加载中...</div>";S.t=n;
  api("GET",n).then(function(d){S.d=d.data;renderT()})["catch"](function(e){c.innerHTML="<div class=\"admin-error\"><p>加载失败: "+e.message+"</p><button onclick=\"loadTable(S.t)\">重试</button></div>"})
}

function renderT(){
  var c=GI("admin-table-container"),d=S.d;
  if(!d||d.length===0){c.innerHTML="<div class=\"admin-empty-state\"><p>暂无数据</p><button data-action=\"new\" class=\"admin-btn admin-btn-primary\">添加</button></div>";return}
  var cfg=ADMIN_TABLES.find(function(t){return t.n===S.t}),cols=cfg.e.slice(0,6);
  var h="<table class=\"admin-table\"><thead><tr><th>ID</th>";
  cols.forEach(function(c){h+="<th>"+c+"</th>"});
  h+="<th>操作</th></tr></thead><tbody>";
  d.forEach(function(r){
    h+="<tr><td>"+(r.id||r.key)+"</td>";
    cols.forEach(function(c){
      var v=r[c];if(v==null)v="";
      if(String(v).length>50)v=String(v).substring(0,50)+"...";
      if(c==="photo"||c==="qr_code"||c==="cover_image"){if(v)v="<img src=\"/uploads/"+v+"\" class=\"admin-thumb\" alt=\"\">"}
      if(c.indexOf("is_")===0)v=v==1?"✓":"✗";
      h+="<td>"+v+"</td>"
    });
    var id=r.id||r.key;
    h+="<td><button data-action=\"edit\" data-id=\""+id+"\" class=\"admin-btn admin-btn-small\">编辑</button>";
    if(!cfg.nd)h+="<button data-action=\"delete\" data-id=\""+id+"\" class=\"admin-btn admin-btn-small admin-btn-danger\">删除</button>";
    h+="</td></tr>"
  });
  h+="</tbody></table>";c.innerHTML=h
}

function showForm(id){
  S.id=id?String(id):null;var cfg=ADMIN_TABLES.find(function(t){return t.n===S.t}),item={};
  if(id){var row=S.d.find(function(r){return(r.id||r.key)==id});if(row)item=row}
  var h="<div class=\"admin-overlay\"><div class=\"admin-form\"><h3>"+(id?"编辑:":"新增:")+cfg.l+"</h3>";
  cfg.e.forEach(function(f){
    var val=item[f]||"",type="text";
    if(f.indexOf("content")>=0)type="textarea";
    if(f.indexOf("is_")===0)type="checkbox";
    if(f==="sort_order"||f==="featured_sort_order")type="number";
    if(f==="article_type")type="select";
    if(f==="report_type")type="select";
    if(f==="type")type="select";
    if(f==="achievements")type="achievements";
    h+="<div class=\"admin-form-group\"><label>"+f+"</label>";
    if(type==="textarea"){h+="<textarea name=\""+f+"\">"+val+"</textarea>"}
    else if(type==="checkbox"){h+="<label><input type=\"checkbox\" name=\""+f+"\" value=\"1\""+(val==1?" checked":"")+"> 启用</label>"}
    else if(type==="number"){h+="<input type=\"number\" name=\""+f+"\" value=\""+val+"\">"}
    else if(type==="select"){
      var opts=[];
      if(f==="article_type")opts=[["news","新闻动态"],["event","活动动态"]];
      else if(f==="report_type")opts=[["research","研究报告"],["life_story","残障生命故事"]];
      else if(f==="type")opts=[["book","手册/图书"],["tool","工具/资源"]];
      h+="<select name=\""+f+"\">"+opts.map(function(o){return '<option value="\""+o[0]+"\""+(val===o[0]?" selected":"")+"\">'+o[1]+'</option>'}).join("")+"</select>"
    }
    else if(type==="achievements"){
      h+='<div id="achievements-editor" class="achievements-editor">';
      var items=[];
      try{items=JSON.parse(val)||[]}catch(e){items=[]}
      if(items.length===0)items=[{title:"",url:""}];
      items.forEach(function(it,i){
        h+='<div class="achievement-row" style="display:flex;gap:8px;margin-bottom:8px;">';
        h+='<input type="text" class="ach-title" placeholder="成果标题" value="\""+escAttr(it.title)+"\"" style="flex:2;">';
        h+='<input type="text" class="ach-url" placeholder="链接地址(如 /report/xxx)" value="\""+escAttr(it.url)+"\"" style="flex:3;">';
        h+='<button data-action="remove-ach" class="admin-btn admin-btn-danger admin-btn-small" type="button">x</button>';
        h+='</div>'
      });
      h+='<button data-action="add-ach" class="admin-btn admin-btn-small" type="button">+ 添加成果</button>';
      h+='</div>'
    }
    else{
      var isU=f.indexOf("photo")>=0||f.indexOf("qr_code")>=0||f.indexOf("cover_image")>=0||f==="pdf_filename"||f==="file_url"||f==="featured_image";
      h+="<div class=\"admin-upload-wrapper\"><input type=\"text\" name=\""+f+"\" value=\""+val+"\">";
      if(isU)h+="<button data-action=\"upload\" data-field=\""+f+"\" data-table=\""+S.t+"\" class=\"admin-btn admin-upload-btn\">上传</button>";
      h+="</div>";if(isU&&val&&f!="pdf_filename"&&f!="file_url")h+="<div class=\"admin-upload-preview\"><img src=\"/uploads/"+val+"\" alt=\"\"></div>"
    }
    h+="</div>"
  });
  h+="<div class=\"admin-form-actions\"><button data-action=\"save\" class=\"admin-btn admin-btn-primary\">保存</button><button data-action=\"cancel\" class=\"admin-btn\">取消</button></div></div></div>";
  GI("admin-overlay-container").innerHTML=h;
  // Setup achievements add/remove handlers
  if(document.getElementById("achievements-editor")){
    document.getElementById("achievements-editor").addEventListener("click",function(ev){
      if(ev.target.dataset.action==="add-ach"){
        var d=document.createElement("div");d.className="achievement-row";d.style="display:flex;gap:8px;margin-bottom:8px;";
        d.innerHTML='<input type="text" class="ach-title" placeholder="成果标题" style="flex:2;"><input type="text" class="ach-url" placeholder="链接地址(如 /report/xxx)" style="flex:3;"><button data-action="remove-ach" class="admin-btn admin-btn-danger admin-btn-small" type="button">x</button>';
        ev.target.parentNode.insertBefore(d,ev.target)
      }
      if(ev.target.dataset.action==="remove-ach"){
        var rows=ev.target.parentNode.parentNode.querySelectorAll(".achievement-row");
        if(rows.length>1)ev.target.parentNode.remove();else{ev.target.parentNode.querySelector(".ach-title").value="";ev.target.parentNode.querySelector(".ach-url").value=""}
      }
    })
  }
}

function closeForm(){GI("admin-overlay-container").innerHTML=""}

function saveForm(){
  var cfg=ADMIN_TABLES.find(function(t){return t.n===S.t}),form=Q(".admin-form"),data={};
  cfg.e.forEach(function(f){
    if(f==="achievements"){
      var rows=form.querySelectorAll(".achievement-row"),items=[];
      rows.forEach(function(r){var t=r.querySelector(".ach-title").value.trim(),u=r.querySelector(".ach-url").value.trim();if(t)items.push({title:t,url:u})});
      data[f]=JSON.stringify(items);
      return
    }
    var el=form.querySelector("[name=\""+f+"\"]");if(el){if(el.type==="checkbox")data[f]=el.checked?1:0;else if(el.tagName==="SELECT")data[f]=el.value;else data[f]=el.value}
  });
  var method=S.id?"PUT":"POST",path=S.id?S.t+"/"+S.id:S.t;
  api(method,path,data).then(function(r){if(r.ok){showToast("保存成功","success");closeForm();loadTable(S.t)}else showToast(r.error||"保存失败","error")})["catch"](function(e){showToast("网络错误","error")})
}

function deleteItem(id){
  api("DELETE",S.t+"/"+id).then(function(r){if(r.ok){showToast("删除成功","success");loadTable(S.t)}else showToast(r.error||"删除失败","error")})
}

function uploadFile(field,table){
  var inp=document.createElement("input");inp.type="file";
  var isImg=field.indexOf("photo")>=0||field.indexOf("qr_code")>=0||field.indexOf("cover_image")>=0;
  inp.accept=isImg?"image/jpeg,image/png":"application/pdf";
  inp.onchange=function(e){
    var file=e.target.files[0];if(!file)return;
    var maxSize=field==="pdf_filename"?20*1024*1024:5*1024*1024;
    if(file.size>maxSize){showToast("文件超过大小限制","error");return}
    var fmr=new FormData();fmr.append("file",file);
    fetch("/upload",{method:"POST",body:fmr}).then(function(r){return r.json()}).then(function(r){
      if(r.ok){
        var inpF=Q("[name=\""+field+"\"]");if(inpF)inpF.value=r.filename;
        var prv=Q(".admin-upload-preview");if(prv&&isImg)prv.innerHTML="<img src=\"/uploads/"+r.filename+"\" alt=\"\">";
        showToast("上传成功","success")
      }else showToast(r.error||"上传失败","error")
    })
  };inp.click()
}

function escAttr(s){return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}

function showToast(msg,type){
  var old=Q(".admin-toast");if(old)old.remove();
  var t=document.createElement("div");t.className="admin-toast admin-toast-"+type;t.textContent=msg;
  document.body.appendChild(t);setTimeout(function(){t.remove()},2500)
}

function renderNav(){
  var h="";ADMIN_TABLES.forEach(function(t){var a=t.n===S.t?" active":"";h+="<button data-action=\"tab\" data-table=\""+t.n+"\""+a+">"+t.l+"</button>"});
  Q(".admin-nav").innerHTML=h
}

function switchTable(n){S.t=n;renderNav();loadTable(n)}

GI("admin-app").addEventListener("click",function(e){
  var btn=e.target.closest("[data-action]");if(!btn)return;
  switch(btn.dataset.action){
    case"tab":switchTable(btn.dataset.table);break;
    case"edit":showForm(btn.dataset.id);break;
    case"new":showForm(null);break;
    case"delete":if(confirm("确定删除?"))deleteItem(btn.dataset.id);break;
    case"save":saveForm();break;
    case"cancel":closeForm();break;
    case"upload":uploadFile(btn.dataset.field,btn.dataset.table);break
  }
})

document.addEventListener("DOMContentLoaded",function(){renderNav();loadTable("site_settings")})