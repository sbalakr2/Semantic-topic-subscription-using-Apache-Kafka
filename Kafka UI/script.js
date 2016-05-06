
//document.getElementById('content').style.height = (document.body.clientHeight - document.getElementById('top-part').offsetHeight);
loadData(document.getElementById('topic-option'));
function loadData(selected){
	document.getElementById('article-list').innerHTML = "";
	var category = selected.options[selected.selectedIndex].value;
	console.log(category);
	var articleArr = data.news_articles;
	var len = articleArr.length;
	for(var i=0; i<len; i++){
			var obj = articleArr[i];
			var cat = obj.class.toLowerCase();
			if(cat.valueOf() == category.valueOf()){
				var article = obj.article.replace(/(<([^>]+)>)/ig,"");
				var _li = document.createElement('li');
				_li.className = 'article-item';
				var _span = document.createElement('span');
				_span.className = 'article-span';
				var _catSpan = document.createElement('span');
				_catSpan.className = 'category-span';
				var _timeSpan = document.createElement('span');
				_timeSpan.className = 'category-span';
				var _txtCat = document.createTextNode(obj.category);
				var _a = document.createElement('a');
				_a.href = obj.url;
				_a.target = '_blank';
				_a.appendChild(_txtCat);
				_catSpan.appendChild(_a);
				var _txt = document.createTextNode(article);
				var _txt1 = document.createTextNode(obj.latency);
				_timeSpan.appendChild(_txt1);
				_span.appendChild(_txt);
				_li.appendChild(_span);
				_li.appendChild(_catSpan);
				_li.appendChild(_timeSpan);
				document.getElementById('article-list').appendChild(_li);
			}
	}
}

function resizeFunc(){
	
}