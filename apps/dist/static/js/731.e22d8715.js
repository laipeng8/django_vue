"use strict";(self["webpackChunkbpvank_front_end"]=self["webpackChunkbpvank_front_end"]||[]).push([[731],{4731:function(e,l,a){a.r(l),a.d(l,{default:function(){return Be}});var t=a(3396),i=a(9242),r=a(7139);const o={class:"card-header"},s=(0,t.Uk)(" 文章管理 "),n={class:"hidden-sm-and-down"},u={class:"visible"},c={style:{display:"inline-flex","justify-content":"center","align-items":"center"}},d={class:"el-dropdown-link",style:{color:"#2fa7b9","font-size":"25xp"},title:"菜单"},m={class:"el-dropdown-link",style:{color:"#2fa7b9","font-size":"16px","margin-right":"15px"},title:"菜单"},p=(0,t.Uk)(" 搜索内容 "),g={class:"highlight"},w={class:"highlight"},f={key:1},V={class:"highlight"},b={key:0},h={key:1},_={key:0},v={key:1},y={key:0,style:{color:"#E6A23C"}},I={key:1,style:{color:"#67C23A"}},C={key:2,style:{color:"#F56C6C"}},D=(0,t.Uk)("预览"),k={class:"el-dropdown-link"},A=(0,t.Uk)("审核 "),W=(0,t.Uk)("待审核 "),x=(0,t.Uk)("通过 "),L=(0,t.Uk)("拒绝 "),P=(0,t.Uk)("编辑"),U=(0,t.Uk)("删除"),S={class:"el-pagination__total is-first"};function z(e,l,a,z,E,F){const N=(0,t.up)("Edit"),T=(0,t.up)("el-icon"),R=(0,t.up)("el-col"),O=(0,t.up)("el-input"),B=(0,t.up)("el-option"),H=(0,t.up)("el-select"),M=(0,t.up)("Refresh"),j=(0,t.up)("el-row"),q=(0,t.up)("Grid"),Y=(0,t.up)("el-dropdown-item"),$=(0,t.up)("el-button"),J=(0,t.up)("el-dropdown-menu"),K=(0,t.up)("el-dropdown"),Q=(0,t.up)("el-table-column"),X=(0,t.up)("el-tooltip"),Z=(0,t.up)("el-image"),G=(0,t.up)("Finished"),ee=(0,t.up)("Select"),le=(0,t.up)("CloseBold"),ae=(0,t.up)("el-popconfirm"),te=(0,t.up)("el-table"),ie=(0,t.up)("el-pagination"),re=(0,t.up)("el-card"),oe=(0,t.up)("AddLink"),se=(0,t.up)("AuditLink"),ne=(0,t.up)("PreviewArticle"),ue=(0,t.up)("CompileArticle"),ce=(0,t.Q2)("loading");return(0,t.wg)(),(0,t.iD)(t.HY,null,[(0,t.Wm)(re,{class:"box-card"},{header:(0,t.w5)((()=>[(0,t._)("div",o,[(0,t._)("h3",null,[(0,t.Wm)(T,{style:{"margin-right":"10px"}},{default:(0,t.w5)((()=>[(0,t.Wm)(N)])),_:1}),s]),(0,t._)("div",n,[(0,t.Wm)(j,{gutter:30},{default:(0,t.w5)((()=>[(0,t.Wm)(R,{span:3}),(0,t.Wm)(R,{span:11},{default:(0,t.w5)((()=>[(0,t.Wm)(O,{"prefix-icon":z.Search,modelValue:e.searchValue,"onUpdate:modelValue":l[0]||(l[0]=l=>e.searchValue=l),onKeyup:(0,i.D2)(z.search,["enter","native"]),placeholder:"关键字搜索(回车)"},null,8,["prefix-icon","modelValue","onKeyup"])])),_:1}),(0,t.Wm)(R,{span:7},{default:(0,t.w5)((()=>[(0,t.Wm)(H,{modelValue:e.auditValue,"onUpdate:modelValue":l[1]||(l[1]=l=>e.auditValue=l),placeholder:"审核筛选"},{default:(0,t.w5)((()=>[(0,t.Wm)(B,{label:"全部",value:"0"}),(0,t.Wm)(B,{label:"待审核",value:"1"}),(0,t.Wm)(B,{label:"已通过",value:"2"}),(0,t.Wm)(B,{label:"已拒绝",value:"3"})])),_:1},8,["modelValue"])])),_:1}),(0,t.Wm)(R,{span:3,style:{display:"inline-flex","justify-content":"center","align-items":"center"}},{default:(0,t.w5)((()=>[(0,t.Wm)(T,{style:{"font-size":"20px",color:"#b3b6bc"},onClick:z.refresh},{default:(0,t.w5)((()=>[(0,t.Wm)(M)])),_:1},8,["onClick"])])),_:1})])),_:1})]),(0,t._)("div",u,[(0,t._)("p",c,[(0,t.Wm)(K,{style:{"line-height":"0px"},"hide-on-click":!1,trigger:"click"},{dropdown:(0,t.w5)((()=>[(0,t.Wm)(J,{class:"visible"},{default:(0,t.w5)((()=>[(0,t.Wm)(Y,null,{default:(0,t.w5)((()=>[(0,t.Wm)(H,{modelValue:e.auditValue,"onUpdate:modelValue":l[2]||(l[2]=l=>e.auditValue=l),placeholder:"审核筛选"},{default:(0,t.w5)((()=>[(0,t.Wm)(B,{label:"全部",value:"0"}),(0,t.Wm)(B,{label:"待审核",value:"1"}),(0,t.Wm)(B,{label:"已通过",value:"2"}),(0,t.Wm)(B,{label:"已拒绝",value:"3"})])),_:1},8,["modelValue"])])),_:1}),(0,t.Wm)(Y,null,{default:(0,t.w5)((()=>[(0,t.Wm)($,{plain:"",style:{width:"100%"},color:"#2fa7b9",onClick:z.openSearch},{default:(0,t.w5)((()=>[p])),_:1},8,["onClick"])])),_:1})])),_:1})])),default:(0,t.w5)((()=>[(0,t._)("span",d,[(0,t._)("span",m,[(0,t.Wm)(T,null,{default:(0,t.w5)((()=>[(0,t.Wm)(q)])),_:1})])])])),_:1}),(0,t.Wm)(T,{onClick:z.refresh},{default:(0,t.w5)((()=>[(0,t.Wm)(M)])),_:1},8,["onClick"])])])])])),default:(0,t.w5)((()=>[(0,t._)("div",null,[(0,t.wy)(((0,t.wg)(),(0,t.j4)(te,{"element-loading-text":"玩命加载中...",data:e.tableData,style:{width:"100%","text-align":"center"},"cell-style":{textAlign:"center"},"row-class-name":e.rowClassName,"header-cell-style":{fontSize:"15px",background:"#2fa7b9",color:"white",textAlign:"center"}},{default:(0,t.w5)((()=>[(0,t.Wm)(Q,{label:"序号",width:"100",type:"index",index:z.Nindex},null,8,["index"]),(0,t.Wm)(Q,{label:"作者"},{default:(0,t.w5)((e=>[(0,t.Wm)(X,{content:e.row.userName,placement:"top",effect:"light"},{default:(0,t.w5)((()=>[(0,t._)("span",g,(0,r.zw)(e.row.userName),1)])),_:2},1032,["content"])])),_:1}),(0,t.Wm)(Q,{label:"标题"},{default:(0,t.w5)((e=>[(0,t.Wm)(X,{content:e.row.articleTitle,placement:"top",effect:"light"},{default:(0,t.w5)((()=>[(0,t._)("span",w,(0,r.zw)(e.row.articleTitle),1)])),_:2},1032,["content"])])),_:1}),(0,t.Wm)(Q,{label:"缩略图"},{default:(0,t.w5)((e=>[e.row.articleImgLitimg?((0,t.wg)(),(0,t.j4)(Z,{key:0,style:{width:"70px"},src:e.row.articleImgLitimg,fit:"cover","preview-teleported":"true","preview-src-list":[e.row.articleImgLitimg]},null,8,["src","preview-src-list"])):(0,t.kq)("",!0),e.row.articleImgLitimg?(0,t.kq)("",!0):((0,t.wg)(),(0,t.iD)("span",f,"无"))])),_:1}),(0,t.Wm)(Q,{label:"分类"},{default:(0,t.w5)((e=>[(0,t.Wm)(X,{content:e.row.articleClassifyName,placement:"top",effect:"light"},{default:(0,t.w5)((()=>[(0,t._)("span",V,(0,r.zw)(e.row.articleClassifyName),1)])),_:2},1032,["content"])])),_:1}),(0,t.Wm)(Q,{label:"文章状态"},{default:(0,t.w5)((e=>[1==e.row.articleState?((0,t.wg)(),(0,t.iD)("div",b,"所有人可见")):(0,t.kq)("",!0),2==e.row.articleState?((0,t.wg)(),(0,t.iD)("div",h,"仅自己可见")):(0,t.kq)("",!0)])),_:1}),(0,t.Wm)(Q,{label:"评论状态"},{default:(0,t.w5)((e=>[1==e.row.commentState?((0,t.wg)(),(0,t.iD)("div",_,"开启")):(0,t.kq)("",!0),2==e.row.commentState?((0,t.wg)(),(0,t.iD)("div",v,"关闭")):(0,t.kq)("",!0)])),_:1}),(0,t.Wm)(Q,{prop:"click",label:"浏览量"}),(0,t.Wm)(Q,{label:"审核状态"},{default:(0,t.w5)((e=>[1==e.row.articlePass?((0,t.wg)(),(0,t.iD)("div",y,"待审核")):(0,t.kq)("",!0),2==e.row.articlePass?((0,t.wg)(),(0,t.iD)("div",I,"已通过")):(0,t.kq)("",!0),3==e.row.articlePass?((0,t.wg)(),(0,t.iD)("div",C,"已拒绝")):(0,t.kq)("",!0)])),_:1}),(0,t.Wm)(Q,{label:"操作",width:"150"},{default:(0,t.w5)((l=>[(0,t.Wm)($,{size:"small",onClick:e=>z.openPreview(l.$index,l.row),style:{margin:"0 0 10px 10px"}},{default:(0,t.w5)((()=>[D])),_:2},1032,["onClick"]),(0,t.Wm)(K,{trigger:"click"},{dropdown:(0,t.w5)((()=>[(0,t.Wm)(J,null,{default:(0,t.w5)((()=>[(0,t.Wm)(Y,{onClick:e=>z.audit(l.row,1)},{default:(0,t.w5)((()=>[(0,t.Wm)(T,null,{default:(0,t.w5)((()=>[(0,t.Wm)(G)])),_:1}),W])),_:2},1032,["onClick"]),(0,t.Wm)(Y,{onClick:e=>z.audit(l.row,2)},{default:(0,t.w5)((()=>[(0,t.Wm)(T,null,{default:(0,t.w5)((()=>[(0,t.Wm)(ee)])),_:1}),x])),_:2},1032,["onClick"]),(0,t.Wm)(Y,{onClick:e=>z.audit(l.row,3)},{default:(0,t.w5)((()=>[(0,t.Wm)(T,null,{default:(0,t.w5)((()=>[(0,t.Wm)(le)])),_:1}),L])),_:2},1032,["onClick"])])),_:2},1024)])),default:(0,t.w5)((()=>[(0,t._)("span",k,[0==e.userInfo.userType?((0,t.wg)(),(0,t.j4)($,{key:0,size:"small",style:{margin:"0 0 10px 10px"}},{default:(0,t.w5)((()=>[A])),_:1})):(0,t.kq)("",!0)])])),_:2},1024),(0,t.Wm)($,{size:"small",onClick:e=>z.openCompile(l.$index,l.row),style:{margin:"0 0 10px 10px"}},{default:(0,t.w5)((()=>[P])),_:2},1032,["onClick"]),(0,t.Wm)(ae,{"confirm-button-text":"确定","cancel-button-text":"取消",icon:z.Delete,"icon-color":"#626AEF",title:"确定删除“"+l.row.articleTitle+"”文章吗？",onConfirm:a=>e.handleDelete(l.$index,l.row)},{reference:(0,t.w5)((()=>[(0,t.Wm)($,{size:"small",type:"danger",style:{"margin-bottom":"10px"}},{default:(0,t.w5)((()=>[U])),_:1})])),_:2},1032,["icon","title","onConfirm"])])),_:1})])),_:1},8,["data","row-class-name"])),[[ce,e.loading]]),(0,t._)("div",null,[(0,t.wy)((0,t.Wm)(ie,{background:"",modelValue:e.currentPage,"onUpdate:modelValue":l[3]||(l[3]=l=>e.currentPage=l),modelModifiers:{"sync:current-page":!0},"page-size":5,"page-sizes":[5],layout:"slot, prev, pager, next, sizes, jumper",total:e.total,onSizeChange:e.handleSizeChange,onCurrentChange:z.changePage,currentPage:e.currentPage,"onUpdate:currentPage":l[4]||(l[4]=l=>e.currentPage=l)},{default:(0,t.w5)((()=>[(0,t._)("span",S," 共 "+(0,r.zw)(e.total)+" 条记录 当前显示第 "+(0,r.zw)(e.currentPage)+" 页记录 ",1)])),_:1},8,["modelValue","total","onSizeChange","onCurrentChange","currentPage"]),[[i.F8,e.total>5]])])])])),_:1}),(0,t.Wm)(oe,{addLinkDialogFormVisible:e.dialogFormVisible.addLinkDialogFormVisible,onOnAddLinkCloseDialog:e.addLinkCloseDialogVisible},null,8,["addLinkDialogFormVisible","onOnAddLinkCloseDialog"]),(0,t.Wm)(se,{auditLinkInfo:e.auditLinkInfo,auditLinkDialogFormVisible:e.dialogFormVisible.auditLinkDialogFormVisible,onOnAuditLinkCloseDialog:z.auditLinkCloseDialogVisible},null,8,["auditLinkInfo","auditLinkDialogFormVisible","onOnAuditLinkCloseDialog"]),(0,t.Wm)(ne,{previewArticleDialogFormVisible:e.previewArticleDialogFormVisible,valueHtml:e.currentArticles,onOnPreviewArticleCloseDialog:z.previewArticleCloseDialog},null,8,["previewArticleDialogFormVisible","valueHtml","onOnPreviewArticleCloseDialog"]),(0,t.Wm)(ue,{compileArticleDialogFormVisible:e.compileArticleDialogFormVisible,valueHtml:e.currentArticles,onOnCompileArticleCloseDialog:z.compileArticleCloseDialog},null,8,["compileArticleDialogFormVisible","valueHtml","onOnCompileArticleCloseDialog"])],64)}a(6699);const E=e=>((0,t.dD)("data-v-41853b8d"),e=e(),(0,t.Cn)(),e),F={key:0},N={class:"articleDase"},T=E((()=>(0,t._)("h3",null,"文章摘要：",-1))),R=E((()=>(0,t._)("div",{class:"articleDase"},[(0,t._)("h3",null,"文章内容：")],-1))),O=["innerHTML"],B={class:"dialog-footer"},H=(0,t.Uk)("退出预览");function M(e,l,a,i,o,s){const n=(0,t.up)("el-button"),u=(0,t.up)("el-dialog"),c=(0,t.Q2)("highlight");return i.isRouterAlive?((0,t.wg)(),(0,t.iD)("div",F,[(0,t.Wm)(u,{modelValue:a.previewArticleDialogFormVisible,"onUpdate:modelValue":l[1]||(l[1]=e=>a.previewArticleDialogFormVisible=e),title:"预览文章",draggable:"",onClose:l[2]||(l[2]=e=>i.previewArticleCloseDialog(!1))},{footer:(0,t.w5)((()=>[(0,t._)("span",B,[(0,t.Wm)(n,{onClick:l[0]||(l[0]=e=>i.previewArticleCloseDialog(!1))},{default:(0,t.w5)((()=>[H])),_:1})])])),default:(0,t.w5)((()=>[(0,t._)("div",N,[T,(0,t._)("p",null,(0,r.zw)(e.articleInfo.articleDase),1)]),R,(0,t.wy)((0,t._)("div",{innerHTML:e.articleInfo.articleContent,class:"article"},null,8,O),[[c]])])),_:1},8,["modelValue"])])):(0,t.kq)("",!0)}var j=a(4870),q={props:["previewArticleDialogFormVisible","valueHtml"],emits:["onPreviewArticleCloseDialog"],setup(e,{emit:l}){(0,t.YP)((()=>e.valueHtml),((e,l)=>{console.log(e),a.articleInfo=e}));const a=(0,j.qj)({previewArticleDialogFormVisible:e.previewArticleDialogFormVisible,articleInfo:e.valueHtml}),i=(0,j.iH)(!0),r=e=>{l("onPreviewArticleCloseDialog",e),i.value=!1,(0,t.Y3)((()=>{i.value=!0}))};return{...(0,j.BK)(a),previewArticleCloseDialog:r,isRouterAlive:i}}},Y=a(89);const $=(0,Y.Z)(q,[["render",M],["__scopeId","data-v-41853b8d"]]);var J=$;const K=e=>((0,t.dD)("data-v-06126f10"),e=e(),(0,t.Cn)(),e),Q={class:"addArticle_box"},X={style:{color:"#2fa7b9","margin-bottom":"10px",padding:"20px 20px","background-color":"white"}},Z=(0,t.Uk)(" 编辑文章 "),G={class:"write_abstract"},ee=K((()=>(0,t._)("h4",null,"标题",-1))),le=K((()=>(0,t._)("p",null,"标示文章、作品内容的简明语句，填写醒目的",-1))),ae={class:"write_abstract"},te={class:"write_abstract"},ie=K((()=>(0,t._)("h4",null,"摘要",-1))),re=K((()=>(0,t._)("p",null,"筛选文章主要内容，让读者初步了解文章",-1))),oe={class:"write_abstract"},se=K((()=>(0,t._)("h4",null,"缩略图",-1))),ne=(0,t.Uk)("上传图片"),ue=K((()=>(0,t._)("p",null,"注：点击上传的图片地址由系统生成，修改会导致图片失效",-1))),ce={class:"write_abstract"},de=K((()=>(0,t._)("h4",null,"分类",-1))),me=K((()=>(0,t._)("p",null,"选择分类可让读者更便捷的查找文章",-1))),pe={class:"write_abstract"},ge=K((()=>(0,t._)("h4",null,"状态",-1))),we=K((()=>(0,t._)("p",null,"私密可视为草稿",-1))),fe={class:"write_abstract"},Ve=K((()=>(0,t._)("h4",null,"评论",-1))),be=K((()=>(0,t._)("p",null,"开启评论，开启新世界",-1))),he={class:"write_abstract",style:{"text-align":"center",background:"none"}},_e=(0,t.Uk)("提交"),ve=K((()=>(0,t._)("p",null,"注：普通用户修改内容需要再次等待管理员审核",-1))),ye=K((()=>(0,t._)("p",{style:{"line-height":"10px"}},"（仅修改分类、状态、评论无须再次等待审核）",-1)));function Ie(e,l,a,i,r,o){const s=(0,t.up)("EditPen"),n=(0,t.up)("el-icon"),u=(0,t.up)("el-input"),c=(0,t.up)("Toolbar"),d=(0,t.up)("Editor"),m=(0,t.up)("el-col"),p=(0,t.up)("el-button"),g=(0,t.up)("el-upload"),w=(0,t.up)("el-option"),f=(0,t.up)("el-select"),V=(0,t.up)("el-row"),b=(0,t.up)("el-dialog");return(0,t.wg)(),(0,t.iD)("div",null,[(0,t.Wm)(b,{modelValue:a.compileArticleDialogFormVisible,"onUpdate:modelValue":l[7]||(l[7]=e=>a.compileArticleDialogFormVisible=e),title:"",width:"85%",onClose:l[8]||(l[8]=e=>i.compileArticleCloseDialog(!1))},{default:(0,t.w5)((()=>[(0,t._)("div",Q,[(0,t._)("h3",X,[(0,t.Wm)(n,{style:{"margin-right":"10px"}},{default:(0,t.w5)((()=>[(0,t.Wm)(s)])),_:1}),Z]),(0,t.Wm)(V,{gutter:20},{default:(0,t.w5)((()=>[(0,t.Wm)(m,{xs:24,sm:24,md:24,lg:17,xl:17},{default:(0,t.w5)((()=>[(0,t._)("div",G,[ee,(0,t.Wm)(u,{modelValue:e.write.titleValue,"onUpdate:modelValue":l[0]||(l[0]=l=>e.write.titleValue=l),placeholder:"请输入文章标题",maxlength:"50","show-word-limit":"",size:"large",clearable:""},null,8,["modelValue"]),le]),(0,t._)("div",ae,[(0,t.Wm)(c,{editor:i.editorRef,defaultConfig:i.toolbarConfig,mode:i.mode},null,8,["editor","defaultConfig","mode"]),(0,t.Wm)(d,{style:{height:"480px","overflow-y":"hidden"},modelValue:i.valueHtml,"onUpdate:modelValue":l[1]||(l[1]=e=>i.valueHtml=e),defaultConfig:i.editorConfig,mode:i.mode,onOnCreated:i.handleCreated,onChange:e.change,class:"article"},null,8,["modelValue","defaultConfig","mode","onOnCreated","onChange"])])])),_:1}),(0,t.Wm)(m,{xs:24,sm:24,md:24,lg:7,xl:7},{default:(0,t.w5)((()=>[(0,t._)("div",te,[ie,(0,t.Wm)(u,{modelValue:e.write.abstractValue,"onUpdate:modelValue":l[2]||(l[2]=l=>e.write.abstractValue=l),autosize:{minRows:3,maxRows:5},maxlength:"200","show-word-limit":"",type:"textarea",placeholder:"请简单概述文章内容",clearable:""},null,8,["modelValue"]),re]),(0,t._)("div",oe,[se,(0,t.Wm)(u,{size:"large",modelValue:e.write.thumbnailValue,"onUpdate:modelValue":l[3]||(l[3]=l=>e.write.thumbnailValue=l),placeholder:"请点击上传图片或手动输入图片地址"},{append:(0,t.w5)((()=>[(0,t.Wm)(g,{ref:"uploadEle",class:"upload-demo",action:e.uploadURL,"on-success":i.handleAvatarSuccess,"before-upload":i.beforeUploadFunction,"show-file-list":!1},{trigger:(0,t.w5)((()=>[(0,t.Wm)(p,null,{default:(0,t.w5)((()=>[ne])),_:1})])),_:1},8,["action","on-success","before-upload"])])),_:1},8,["modelValue"]),ue]),(0,t._)("div",ce,[de,(0,t.Wm)(f,{modelValue:e.write.classifyValue,"onUpdate:modelValue":l[4]||(l[4]=l=>e.write.classifyValue=l),placeholder:"请选择文章分类",size:"large"},{default:(0,t.w5)((()=>[((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)(e.classifyInfo,(e=>((0,t.wg)(),(0,t.j4)(w,{label:e.classifyName,value:e.classifyId},null,8,["label","value"])))),256))])),_:1},8,["modelValue"]),me]),(0,t.Wm)(V,{gutter:20},{default:(0,t.w5)((()=>[(0,t.Wm)(m,{xs:24,sm:12,md:12,lg:12,xl:12},{default:(0,t.w5)((()=>[(0,t._)("div",pe,[ge,(0,t.Wm)(f,{modelValue:e.write.stateValue,"onUpdate:modelValue":l[5]||(l[5]=l=>e.write.stateValue=l),placeholder:"文章状态",size:"large"},{default:(0,t.w5)((()=>[(0,t.Wm)(w,{label:"公开",value:"1"}),(0,t.Wm)(w,{label:"私密",value:"2"})])),_:1},8,["modelValue"]),we])])),_:1}),(0,t.Wm)(m,{xs:24,sm:12,md:12,lg:12,xl:12},{default:(0,t.w5)((()=>[(0,t._)("div",fe,[Ve,(0,t.Wm)(f,{modelValue:e.write.commentValue,"onUpdate:modelValue":l[6]||(l[6]=l=>e.write.commentValue=l),placeholder:"评论是否开启",size:"large"},{default:(0,t.w5)((()=>[(0,t.Wm)(w,{label:"开启",value:"1"}),(0,t.Wm)(w,{label:"关闭",value:"2"})])),_:1},8,["modelValue"]),be])])),_:1})])),_:1}),(0,t._)("div",he,[(0,t.Wm)(p,{style:{width:"50%"},plain:"",color:"#2fa7b9",onClick:i.submitupdate},{default:(0,t.w5)((()=>[_e])),_:1},8,["onClick"]),ve,ye])])),_:1})])),_:1})])])),_:1},8,["modelValue"])])}var Ce=a(6126),De=a(7178),ke=a(6666),Ae=a(6265),We=a.n(Ae);function xe(e){We().get("/showAllClassifyInfo").then((l=>{e.classifyInfo=l.data.data}))}var Le={components:{Editor:Ce.M,Toolbar:Ce.o},props:["compileArticleDialogFormVisible","valueHtml"],emits:["onCompileArticleCloseDialog"],setup(e,{emit:l}){const a=(0,j.XI)(),i=(0,j.iH)(""),r={},o={placeholder:"在myblog，开始您的Write吧~",MENU_CONF:{}};(0,t.YP)(i.value,(function(e,l){Prism.highlightAll()})),(0,t.Jd)((()=>{const e=a.value;null!=e&&e.destroy()}));const s=e=>{a.value=e};o.MENU_CONF["uploadImage"]={server:{NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL+"/articleImgUpload",maxFileSize:5242880,onFailed(e,l){De.z8.error(`${e.name} 上传失败`)}},o.MENU_CONF["uploadVideo"]={server:{NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL+"articleVideoUpload",maxFileSize:104857600,onFailed(e,l){De.z8.error(`${e.name} 上传失败`)}},o.MENU_CONF["codeSelectLang"]={codeLangs:[{text:"CSS",value:"css"},{text:"HTML",value:"html"},{text:"XML",value:"xml"},{text:"Javascript",value:"javascript"},{text:"Typescript",value:"typescript"},{text:"JSX",value:"jsx"},{text:"Go",value:"go"},{text:"PHP",value:"php"},{text:"C",value:"c"},{text:"Python",value:"python"},{text:"Java",value:"java"},{text:"C++",value:"cpp"},{text:"C#",value:"csharp"},{text:"Visual Basic",value:"visual-basic"},{text:"SQL",value:"sql"},{text:"Ruby",value:"ruby"},{text:"Swift",value:"swift"},{text:"Bash",value:"bash"},{text:"Markdown",value:"markdown"}]},(0,t.YP)((()=>e.valueHtml),((e,l)=>{n.articleInfo=e,i.value=e.articleContent,n.write.titleValue=e.articleTitle,n.write.abstractValue=e.articleDase;var a=e.articleImgLitimg;a.includes("http://101.43.207.70:8080/")?a=a.replaceAll("http://101.43.207.70:8080/",""):a.includes("http://www.bpvank.com:8080/")&&(a=a.replaceAll("http://www.bpvank.com:8080/","")),n.write.thumbnailValue=a,n.write.classifyValue=e.articleClassifyId,n.write.stateValue=e.articleState.toString(),n.write.commentValue=e.commentState.toString()}));const n=(0,j.qj)({compileArticleDialogFormVisible:e.compileArticleDialogFormVisible,articleInfo:e.valueHtml,userInfo:null,write:{titleValue:"",abstractValue:"",thumbnailValue:"",classifyValue:"",stateValue:"",commentValue:""},classifyInfo:[],uploadURL:{NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL+"/thumbnailUpload"});(0,t.bv)((()=>{const e=JSON.parse(sessionStorage.getItem("userInfo"));n.userInfo=e.data,xe(n)}));const u=e=>"image/jpeg"!==e.type&&"image/jpg"!==e.type&&"image/png"!==e.type&&"image/gif"!==e.type?(De.z8.error("仅支持图片格式.png | .jpg | .jpeg | .gif "),!1):!(e.size/1024/1024>5)||(De.z8.error("仅支持大小不超过5MB的图片!"),!1),c=e=>{n.write.thumbnailValue=e},d=e=>{l("onCompileArticleCloseDialog",e)},m=()=>{if(n.write.abstractValue!==n.articleInfo.articleDase||n.write.classifyValue!==n.articleInfo.articleClassifyId||parseInt(n.write.stateValue)!==n.articleInfo.articleState||parseInt(n.write.commentValue)!==n.articleInfo.commentState||{NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL+n.write.thumbnailValue!==n.articleInfo.articleImgLitimg&&n.write.thumbnailValue!==n.articleInfo.articleImgLitimg||n.write.titleValue!==n.articleInfo.articleTitle||i.value!==n.articleInfo.articleContent)if(n.write.abstractValue!==n.articleInfo.articleDase||{NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL+n.write.thumbnailValue!==n.articleInfo.articleImgLitimg&&n.write.thumbnailValue!==n.articleInfo.articleImgLitimg||n.write.titleValue!==n.articleInfo.articleTitle||i.value!==n.articleInfo.articleContent||parseInt(n.write.stateValue)===n.articleInfo.articleState&&parseInt(n.write.commentValue)===n.articleInfo.commentState&&n.write.classifyValue===n.articleInfo.articleClassifyId){let e={};if(e=n.classifyInfo.find((e=>e.classifyId===n.write.classifyValue)),""!=n.write.titleValue&&""!=n.write.abstractValue&&""!=n.write.classifyValue&&""!=n.write.stateValue&&""!=n.write.commentValue){const a={articleId:n.articleInfo.articleId,articleTitle:n.write.titleValue,articleClassifyId:n.write.classifyValue,articleClassifyName:e.classifyName,articleDase:n.write.abstractValue,articleImgLitimg:n.write.thumbnailValue,articleContent:i.value,articleState:parseInt(n.write.stateValue),articlePass:0==n.userInfo.userType?2:1,commentState:parseInt(n.write.commentValue)};We().post("/article/updateArticleInfo",a).then((e=>{0==e.data.code&&(i.value="<p><br></p>",n.write={titleValue:"",abstractValue:"",thumbnailValue:"",classifyValue:"",stateValue:"",commentValue:""},(0,ke.bM)({title:"提示",message:0==n.userInfo.userType?"文章修改成功！":"文章修改成功，等待管理员审核展示",type:"success"}),l("onCompileArticleCloseDialog",!1,e.data.code))}))}else De.z8.error("除缩略图之外的内容都是必填项哦~")}else{let e={};if(e=n.classifyInfo.find((e=>e.classifyId===n.write.classifyValue)),""!=n.write.titleValue&&""!=n.write.abstractValue&&""!=n.write.classifyValue&&""!=n.write.stateValue&&""!=n.write.commentValue){n.write.classifyValue!==n.articleInfo.articleClassifyId&&(We().get("/updateArticleNumberByClassifyId",{params:{classifyId:n.write.classifyValue}}),We().get("/updateArticleNumberByClassifyId2",{params:{classifyId:n.articleInfo.articleClassifyId}}));const a={articleId:n.articleInfo.articleId,articleTitle:n.write.titleValue,articleClassifyId:n.write.classifyValue,articleClassifyName:e.classifyName,articleDase:n.write.abstractValue,articleImgLitimg:n.write.thumbnailValue,articleContent:i.value,articleState:parseInt(n.write.stateValue),articlePass:n.articleInfo.articlePass,commentState:parseInt(n.write.commentValue)};We().post("/article/updateArticleInfo",a).then((e=>{0==e.data.code&&(i.value="<p><br></p>",n.write={titleValue:"",abstractValue:"",thumbnailValue:"",classifyValue:"",stateValue:"",commentValue:""},(0,ke.bM)({title:"提示",message:"文章修改成功",type:"success"}),l("onCompileArticleCloseDialog",!1,e.data.code))}))}else De.z8.error("除缩略图之外的内容都是必填项哦~")}else i.value="<p><br></p>",n.write={titleValue:"",abstractValue:"",thumbnailValue:"",classifyValue:"",stateValue:"",commentValue:""},(0,ke.bM)({title:"提示",message:"小样，文章好像没有任何改变哦！",type:"success"}),l("onCompileArticleCloseDialog",!1)};return{...(0,j.BK)(n),compileArticleCloseDialog:d,beforeUploadFunction:u,handleAvatarSuccess:c,editorRef:a,valueHtml:i,mode:"default",toolbarConfig:r,editorConfig:o,handleCreated:s,submitupdate:m}}};const Pe=(0,Y.Z)(Le,[["render",Ie],["__scopeId","data-v-06126f10"]]);var Ue=Pe,Se=a(2748),ze=a(2655);function Ee(e){let l=(e+"").split("");for(let g=0;g<13;g++)l[g]||(l[g]="0");e=1*l.join("");let a=6e4,t=60*a,i=24*t,r=30*i,o=(new Date).getTime(),s=o-e;if(s<0)return"不久前";let n=s/r,u=s/(7*i),c=s/i,d=s/t,m=s/a,p=function(e){return e<10?"0"+e:e};return n>4?function(){let l=new Date(e);return l.getFullYear()+"年"+p(l.getMonth()+1)+"月"+p(l.getDate())+"日"}():n>=1?parseInt(n)+"月前":u>=1?parseInt(u)+"周前":c>=1?parseInt(c)+"天前":d>=1?parseInt(d)+"小时前":m>=1?parseInt(m)+"分钟前":"刚刚"}function Fe(e){e.loading=!0;const l=sessionStorage.getItem("userInfo"),a=JSON.parse(l);e.userInfo=a.data;var t={currentPage:e.currentPage,pageSize:e.pageSize,userType:e.userInfo.userType,userId:e.userInfo.userId};We().get("/article/page/byUserType",{params:t}).then((l=>{e.tableData=[],l.data.data.list.forEach((l=>{l.publishTime=Ee(l.publishTime);const a={NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL;""==l.articleImgLitimg||l.articleImgLitimg.includes("http")||(l.articleImgLitimg=a+l.articleImgLitimg),e.tableData.push(l)})),e.total=l.data.data.total,e.pageSize=l.data.data.pageSize,e.currentPage=l.data.data.currentPage,e.loading=!1}))}function Ne(e){e.loading=!0;var l={currentPage:e.currentPage,pageSize:e.pageSize,userType:e.userInfo.userType,userId:e.userInfo.userId,articleTitle:e.searchValue};We().get("/article/search/title",{params:l}).then((l=>{e.tableData=[],l.data.data.list.forEach((l=>{l.publishTime=Ee(l.publishTime);const a={NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL;""==l.articleImgLitimg||l.articleImgLitimg.includes("http")||l.articleImgLitimg.includes("https")||(l.articleImgLitimg=a+l.articleImgLitimg),e.tableData.push(l)})),e.total=l.data.data.total,e.pageSize=l.data.data.pageSize,e.currentPage=l.data.data.currentPage,e.loading=!1}))}function Te(e){e.loading=!0;var l={currentPage:e.currentPage,pageSize:e.pageSize,userType:e.userInfo.userType,userId:e.userInfo.userId,articlePass:e.auditValue};We().get("/article/search/pass",{params:l}).then((l=>{e.tableData=[],l.data.data.list.forEach((l=>{l.publishTime=Ee(l.publishTime);const a={NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL;""==l.articleImgLitimg||l.articleImgLitimg.includes("http")||l.articleImgLitimg.includes("https")||(l.articleImgLitimg=a+l.articleImgLitimg),e.tableData.push(l)})),e.total=l.data.data.total,e.pageSize=l.data.data.pageSize,e.currentPage=l.data.data.currentPage,e.loading=!1}))}var Re={components:{PreviewArticle:J,CompileArticle:Ue},setup(e){(0,t.bv)((()=>{Fe(a)}));const l={NODE_ENV:"production",BASE_URL:"/"}.VUE_APP_URL,a=(0,j.qj)({userInfo:null,searchValue:"",auditValue:null,tableData:[],dialogFormVisible:{addLinkDialogFormVisible:!1,auditLinkDialogFormVisible:!1,a:1},total:0,pageSize:5,currentPage:1,auditLinkInfo:{},previewArticleDialogFormVisible:!1,compileArticleDialogFormVisible:!1,currentArticles:null,loading:!1}),i=(e,l)=>{a.dialogFormVisible.auditLinkDialogFormVisible=!0,a.auditLinkInfo=l},r=(e,l)=>{a.dialogFormVisible.auditLinkDialogFormVisible=e,void 0!=l&&Fe(a)},o=(e,l)=>{a.previewArticleDialogFormVisible=!0,a.currentArticles=l},s=e=>{a.previewArticleDialogFormVisible=e},n=(e,l)=>{a.compileArticleDialogFormVisible=!0,a.currentArticles=l},u=(e,l)=>{a.compileArticleDialogFormVisible=e,""!==a.searchValue?Ne(a):0!==a.auditValue&&null!=a.auditValue?Te(a):Fe(a)},c=e=>{a.currentPage=e,""!==a.searchValue?Ne(a):0!==a.auditValue&&null!=a.auditValue?Te(a):Fe(a)},d=e=>{const l=a.currentPage,t=a.pageSize;return e+1+(l-1)*t},m=()=>{ze.T.prompt("请输入网站关键字进行搜索","搜索",{confirmButtonText:"搜索",cancelButtonText:"取消",inputErrorMessage:"Invalid Email"}).then((({value:e})=>{a.auditValue=null,a.searchValue=e,Ne(a),null!==e?(0,De.z8)({type:"success",message:`关键字“${e}”搜索内容如下`}):(0,De.z8)({type:"success",message:"已为您清除搜索"})}))},p=()=>{a.auditValue=null,Ne(a),""!==a.searchValue?(0,De.z8)({type:"success",message:`关键字“${a.searchValue}”搜索内容如下`}):(0,De.z8)({type:"success",message:"已为您清除搜索"})};(0,t.YP)((()=>a.auditValue),((e,l)=>{e&&(a.searchValue="",0==a.auditValue?Fe(a):Te(a))}));const g=()=>{a.searchValue="",a.auditValue=null,Fe(a),(0,De.z8)({message:"刷新成功",type:"success"})},w=(e,l)=>{if(e.articlePass!==l){var t={articleId:e.articleId,articlePass:l};We().get("/article/updateArticlePass",{params:t}).then((e=>{"0"==e.data.code?((0,ke.bM)({title:"提示",message:"审核成功",type:"success"}),""!==a.searchValue?Ne(a):0!==a.auditValue&&null!=a.auditValue?Te(a):Fe(a)):De.z8.error("审核失败！")}))}else(0,ke.bM)({title:"提示",message:"小样，好像没有任何改变哦！",type:"success"})};function f(e){const l=(l,a)=>{console.log(a),We()["delete"]("/article/delete",{params:{articleId:a.articleId}}).then((l=>{"0"==l.data.code?(We()["delete"]("/comment/deleteByArticleId",{params:{articleId:a.articleId}}),We().get("/updateArticleNumberByClassifyId2",{params:{classifyId:a.articleClassifyId}}),(0,ke.bM)({title:"提示",message:"已成功删除“"+a.articleTitle+"”文章",type:"success"}),""!==e.searchValue?Ne(e):0!==e.auditValue&&null!=e.auditValue?Te(e):Fe(e)):De.z8.error("文章删除失败")}))};return{handleDelete:l}}return{Search:Se.Search,Delete:Se.Delete,...(0,j.BK)(a),search:p,openSearch:m,auditLink:i,auditLinkCloseDialogVisible:r,openPreview:o,previewArticleCloseDialog:s,openCompile:n,compileArticleCloseDialog:u,changePage:c,...f(a),Nindex:d,url:l,refresh:g,audit:w}}};const Oe=(0,Y.Z)(Re,[["render",z],["__scopeId","data-v-4416de68"]]);var Be=Oe}}]);