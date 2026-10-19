# _plugins/fetch_publications.rb
module Jekyll
  class PublicationsTag < Liquid::Tag
    def render(context)
      require 'net/http'
      require 'uri'
      
      url = "https://rth.dk/publications/get_publications.php?PubWords=Seemann"
      uri = URI(url)
      response = Net::HTTP.get(uri)
      response
    rescue => e
      "Error fetching publications: #{e.message}"
    end
  end
end

Liquid::Template.register_tag('publications', Jekyll::PublicationsTag)
