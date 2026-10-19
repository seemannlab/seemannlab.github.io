# _plugins/fetch_publications.rb
module Jekyll
  class PublicationsGenerator < Generator
    def generate(site)
      # This runs during build
    end
  end

  class PublicationsTag < Liquid::Tag
    def initialize(tag_name, markup, tokens)
      super
      @markup = markup.strip
    end

    def render(context)
      require 'net/http'
      require 'uri'
      
      begin
        url = "https://rth.dk/publications/get_publications.php?PubWords=Seemann"
        uri = URI(url)
        http = Net::HTTP.new(uri.host, uri.port)
        http.use_ssl = true
        request = Net::HTTP::Get.new(uri.request_uri)
        response = http.request(request)
        response.body
      rescue => e
        "<p>Error fetching publications: #{e.message}</p>"
      end
    end
  end
end

Liquid::Template.register_tag('publications', Jekyll::PublicationsTag)
