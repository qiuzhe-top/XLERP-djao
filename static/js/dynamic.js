var fBO = 0;
var yp = 1;
// $(window).scroll(function(){
// 	　　var scrollTop = $(this).scrollTop();
// 	　　var scrollHeight = $(document).height();
// 	　　var windowHeight = $(this).height();
//     // console.log('等待加载中',fBO)
	
// 		console.log(scrollHeight-scrollTop - windowHeight)
// 	　　if(scrollHeight-scrollTop - windowHeight<500 && fBO == 0){
// 		　　//当滚动到底部时,执行此代码框中的代码
// 			var uptop = document.getElementById( "uptop" )
// 			// uptop.style.height=300+'px';
// 			// console.log(uptop.style.height)
// 			console.log('等待加载中',fBO)
// 			fBO = 1
//             myFunction()
//             // var myVar=setTimeout("location.reload()",1000);
//             // alert(0)
            
			
// 	　　}
// 	});

// 	function myFunction() {
// 		setTimeout(function(){ 
// 			console.log('加载完成')
//             fBO = 0
//         }, 5000);


// // //  1 1*10-1 1*10+10
// //  2 2*10+1 2*10+10

//         $.ajax({
//             url:'/postAJ/',
//             type:'POST',
//             data:{data:yp},
//             beforeSend:function(){//加载中

//             },
//             complete:function(){//加载完成

//             },
//             success:function(arg){//加载完成返回数据
//                 console.log(arg)
//             },
//             statusCode: {
//                 200: function() {
//                     // alert('服务器cg。200');
//                     yp+=1;
//                 }
//             }
     
//         })
// 	}