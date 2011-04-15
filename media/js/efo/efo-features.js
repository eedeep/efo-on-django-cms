$(document).ready(function() {
	
	function TabLayout(settings) {
		var	tabContainer = $(settings.tabContainer);
		var tabs = [];
		var active, tabList;
		
		this.addTab = function(t){
			t.tabObject = $(tabContainer.selector + " " + t.tabSelector);
			t.titleObject = $(tabContainer.selector + " " + t.tabSelector + " " + t.titleSelector);	
			if(tabs.length === 0)
			{
				active = t;
			}
			tabs.push(t);
		};
		
		var findByTabTitle = function(t){
			for(var i = 0; i < tabs.length; i++)
			{
				if(t === tabs[i].tabControlLink.html())
					return tabs[i];
			}
			return undefined;
		};
		
		var createTabList = function(){
			tabList = $(document.createElement('ul'));
			tabList.addClass("tab-select");

			for(var i = 0; i < tabs.length; i++)
			{
				var currentTabTitle = $(settings.tabContainer + " " + tabs[i].tabSelector).children($(tabs[i].titleSelector)).html();
				
				tabs[i].tabControlLink = $(document.createElement('a'))
												.attr("href", "#")
												.html(currentTabTitle);
												
				tabs[i].tabControlContainer = $(document.createElement('li'));
										
				if(tabs[i] === active)
				{
					tabs[i].tabControlLink.addClass("active");
				}
				tabs[i].titleObject.hide();
				tabList.append(tabs[i].tabControlContainer);
				tabs[i].tabControlLink.appendTo(tabs[i].tabControlContainer);
				
			}
			tabContainer.prepend(tabList);
			
			$(tabContainer.selector + ' .tab-select a').click(function(){

				for(var i = 0; i < tabs.length; i++)
				{
					tabs[i].tabObject.hide();
					$(tabContainer.selector + ' .tab-select a').removeClass("active");
				}
				
				var clickedTab = findByTabTitle($(this).html());
				clickedTab.tabObject.show();
				$(this).addClass("active");
				return false;
			});
		};
				
		this.display = function(){
			createTabList();
			for(var i = 1; i < tabs.length; i++)
			{
				tabs[i].tabObject.hide();
			}
					
		}
	};

	var asideTabs = new TabLayout({
		tabContainer : ".asides-tabs:first"
	});
	
	asideTabs.addTab({
		tabSelector : ".tab:nth-child(1)",
		titleSelector : "h4"
	});

	asideTabs.addTab({
		tabSelector : ".tab:nth-child(2)",
		titleSelector : "h4"
	});
	
	asideTabs.addTab({
		tabSelector : ".tab:nth-child(3)",
		titleSelector : "h4"
	});
	
	asideTabs.display();
	
	var asideTabsPopularCommented = new TabLayout({
		tabContainer : ".asides-tabs:last"
	});
	
	asideTabsPopularCommented.addTab({
		tabSelector : ".tab:nth-child(1)",
		titleSelector : "h4"
	});

	asideTabsPopularCommented.addTab({
		tabSelector : ".tab:nth-child(2)",
		titleSelector : "h4"
	});
	
	asideTabsPopularCommented.display();
	
	var submitButton = $('#find_submit');
	var searchForm = $("#search");
	var loading = $(".loading"); 
	var searchBox = $('#q');
	
	searchBox.focus(function(){
		$(this).css("color", "#000");
		$(this).val("");
	});
	
	searchBox.blur(function(){
		if($(this).value() === "")
		{
			$(this).css("color", "#9A9A9A");
			$(this).val("search");
		}
	});
	
	submitButton.click(function(){
		$("#search").submit();
		return false;
	});
	
	$("#search").submit(function(){
		loading.css("display", "block");
		$(this).submit();
	});
	
	/*
	
	$('#feature-nav ul li').hover(function() {
	    id = $(this).attr('object_id');
    	
	    $('#feature-nav ul li').removeClass("active");
	    $(this).addClass("active");
    
	    $('#feature-images figure')
	      .each(function(i){
	        $(this).attr('z-index', '-99').fadeTo(100, 0)
	      });
      
	    $('#feature-images figure#feature-' + id + '-figure')
	      .attr('z-index', '99')
	      .show()
	      .fadeTo(100, 100);
	});
  
  	
    // $('#edit-project').hide();
    //     $('#edit-project-toggle').click(function() {
    //         $('#edit-project').toggle();
    //         $('#edit-project').autoscroll();
    //         return false;
    //     });
    //     if ($('#edit-project .error').length) {
    //         $('#edit-project').show();
    //         $('#edit-project .error').autoscroll();
    //     }
    //     $('#add-member').hide();
    //     $('#add-member-toggle').click(function() {
    //         $('#add-member').toggle();
    //         $('#add-member').autoscroll();
    //         return false;
    //     });
    //     if ($('#add-member .error').length) {
    //         $('#add-member').show();
    //         $('#add-member .error').autoscroll();
    //     }

	
	*/
	
});